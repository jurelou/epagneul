import os
import argparse
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def upload_folder_or_file(input_path: str, folder_name: str, console_url: str, console_port: int):
    """
    Uploads a folder or a single file (EVTX or JSONL) to Epagneul.

    Args:
        input_path (str): Path to the folder or file to upload.
        folder_name (str): Name of the folder to create.
        console_url (str): Base URL of Epagneul.
        console_port (int): Port of Epagneul backend.

    Returns:
        None
    """
    # Check if folder already exists, get its identifier
    folders = f"{console_url}:{console_port}/api/folders/"
    logger.info(f"Checking if folder '{folder_name}' exists...")
    list_response = requests.get(folders)
    folder_identifier = None

    if list_response.status_code == 200:
        existing_folders = list_response.json()
        for folder in existing_folders:
            if folder["name"] == folder_name:
                folder_identifier = folder["identifier"]
                logger.info(f"Folder '{folder_name}' already exists with identifier '{folder_identifier}'. Proceeding with upload...")
                break
    else:
        logger.error(f"Failed to fetch folder list: {list_response.status_code}, {list_response.text}")
        return

    # Create folder if it does not exist and get its identifier
    if not folder_identifier:
        create_url = f"{console_url}:{console_port}/api/folders/{folder_name}"
        logger.info(f"Creating folder '{folder_name}'...")
        create_response = requests.post(create_url)
        if create_response.status_code == 200:
            logger.info(f"Folder '{folder_name}' created successfully.")
            logger.info(f"Fetching folder list to retrieve identifier for '{folder_name}'...")
            list_response = requests.get(folders)
            if list_response.status_code == 200:
                existing_folders = list_response.json()
                for folder in existing_folders:
                    if folder["name"] == folder_name:
                        folder_identifier = folder["identifier"]
                        logger.info(f"Retrieved identifier for folder '{folder_name}': {folder_identifier}")
                        break
                if not folder_identifier:
                    logger.error(f"Failed to retrieve identifier for folder '{folder_name}' after creation.")
                    return
            else:
                logger.error(f"Failed to fetch folder list after creation: {list_response.status_code}, {list_response.text}")
                return
        else:
            logger.error(f"Failed to create folder: {create_response.status_code}, {create_response.text}")
            return

    # Construct the full URL for the upload endpoint
    upload_url = f"{console_url}:{console_port}/api/folders/{folder_identifier}/upload"
    files = []

    # Check if input path is a file or folder
    if os.path.isfile(input_path):
        # Validate and prepare a single file for upload
        file_name = os.path.basename(input_path)
        if file_name.endswith(".jsonl") or file_name.endswith(".evtx"):
            file_obj = open(input_path, "rb")
            files.append((file_name, (file_name, file_obj, "application/octet-stream")))
        else:
            logger.error(f"Error: Unsupported file type for '{file_name}'. Only .jsonl and .evtx are allowed.")
            return
    elif os.path.isdir(input_path):
        # Prepare files from the folder
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            if os.path.isfile(file_path) and (file_name.endswith(".jsonl") or file_name.endswith(".evtx")):
                file_obj = open(file_path, "rb")
                files.append((file_name, (file_name, file_obj, "application/octet-stream")))
            else:
                logger.info(f"Skipping unsupported file: {file_name}")
    else:
        logger.error(f"Error: The input path '{input_path}' is neither a valid file nor a folder.")
        return

    if not files:
        logger.info("No valid files (.jsonl or .evtx) found for upload.")
        return

    try:
        # Send POST request
        file_names = [file[0] for file in files]
        logger.info(f"Uploading files: {', '.join(file_names)} to {upload_url}...")
        response = requests.post(upload_url, files=files, verify=False)

        if response.status_code == 200:
            logger.info("Files uploaded successfully")
        else:
            logger.error(f"Failed to upload files: {response.status_code}, {response.text}")
    finally:
        # Close all file objects to release resources
        for _, (file_name, file_obj, _) in files:
            file_obj.close()


def main():
    # Define arguments using argparse
    parser = argparse.ArgumentParser(
        description="Utility to upload a folder or a file containing EVTX and parsed EVTX (JSONL) files to Epagneul."
    )
    parser.add_argument(
        "--input-path",
        type=str,
        required=True,
        help="Path to the folder or file to upload.",
    )
    parser.add_argument(
        "--folder-name",
        type=str,
        required=True,
        help="Name of the folder to create.",
    )
    parser.add_argument(
        "--console-url",
        type=str,
        required=True,
        help="Base URL of Epagneul (e.g., http://127.0.0.1).",
    )
    parser.add_argument(
        "--console-port",
        type=int,
        default=6327,
        help="Port of Epagneul backend (default: 6327).",
    )

    args = parser.parse_args()

    # Call the upload function with parsed arguments
    upload_folder_or_file(args.input_path, args.folder_name, args.console_url, args.console_port)


if __name__ == "__main__":
    main()

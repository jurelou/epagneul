from loguru import logger
from fastapi import Depends, Request, APIRouter, UploadFile, File, HTTPException
import traceback

from epagneul.api.core.neo4j import get_database
from epagneul.models.folders import Folder, Stats, MachineStat, UserStat
from epagneul.models.files import File
from epagneul.models.graph import Edge, Node, EdgeData, NodeData
from epagneul.artifacts.evtx import parse_evtx

router = APIRouter()

@router.get("/")
def get_folders(db = Depends(get_database)):
    print("GET folders")
    return db.get_folders()


@router.get("/{folder_name}")
def get_folder(folder_name: str, db = Depends(get_database)):
    print(f"get folder {folder_name}")
    folder = db.get_folder(folder_name)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")

    folder.nodes, folder.edges = db.get_graph(folder=folder_name)

    users_stats = []
    machines_stats = []
    for node in folder.nodes:
        if node.data.category == "user":
            users_stats.append(UserStat(identifier=node.data.label, pagerank=node.data.algo_pagerank))
        elif node.data.category == "machine":
            machines_stats.append(MachineStat(identifier=node.data.label, pagerank=node.data.algo_pagerank))

    folder.stats = Stats(machines_stats=machines_stats, users_stats=users_stats)
    #identifier=node.data.label, pagerank=node.data.pagerank) for node in nodes if not node.data.is_compound

    return folder


@router.delete("/{folder_name}")
def delete_folder(folder_name: str, db = Depends(get_database)):
    print(f"Remove folder {folder_name}")
    return db.remove_folder(folder_name)

@router.post("/{folder_name}")
def create_folder(folder_name: str, db = Depends(get_database)):
    print(f"Create folder {folder_name}")
    new_folder = Folder(
        name=folder_name,
        summary=f"summ for {folder_name}"
    )
    db.create_folder(new_folder)

    print(f"New folder {folder_name}, {new_folder}")


def analyze_file(db, folder: str, file_data):
    store = parse_evtx(file_data)
    db.add_evtx_store(store, folder=folder)
    db.make_lpa(folder)
    db.make_pagerank(folder)

@router.post("/{folder_name}/upload")
async def upload_folder(folder_name: str, request: Request, db = Depends(get_database)):
    print(f"upload files {folder_name}")
    folder = db.get_folder(folder_name)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")

    form_files = await request.form()
    for filename, filedata in form_files.items():
        db.add_folder_file(folder_name, File(name=filename))
        try:
            analyze_file(db, folder_name, filedata.file)
        except Exception as err:
            print("ERR while parsing evtx", err)
            print(traceback.format_exc())
            raise HTTPException(status_code=500, detail=f"Could not process file {filename} : {str(err)}")


import { api_base_url } from './config';
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

export function deleteFolder(folder_name) {
    return fetch(`${api_base_url}/folders/${folder_name}`, {
        method: 'delete'
    }).then(r => r.json())
}

export function createFolder(folder_name) {
    return fetch(`${api_base_url}/folders/${folder_name}`, {
        method: 'post'
    }).then(r => r.json())
}



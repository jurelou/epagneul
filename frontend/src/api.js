const base_url = process.env.VUE_APP_BASE_URL

export function deleteFolder(folder_name) {
    return fetch(`${base_url}/folders/${folder_name}`, {
        method: 'delete'
    }).then(r => r.json())
}

export function createFolder(folder_name) {
    return fetch(`${base_url}/folders/${folder_name}`, {
        method: 'post'
    }).then(r => r.json())
}



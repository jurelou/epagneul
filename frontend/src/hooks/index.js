import { useQuery } from 'vue-query';

const base_url = process.env.VUE_APP_BASE_URL

export function useFolders() {
	const { data: folders, isLoading, refetch } = useQuery(
		"folders",
		() => fetch(`${base_url}/folders/`).then((r) => r.json()),
		{
			staleTime: 30 * 1000,
		}
	);

	return { folders, isLoading, refetch};
}

export function useFolder(folder_id) {
	const { data: folder, isLoading, refetch, isError } = useQuery(
		["folder", folder_id],
		() => fetch(`${base_url}/folders/${folder_id}`).then((r) => r.json()),
		{
			//staleTime: 30 * 1000,
			refetchOnWindowFocus: false,
			refetchOnReconnect: false

		}
	);

	return { folder, isLoading, refetch, isError};
}

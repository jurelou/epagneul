import { useQuery } from 'vue-query';
import { api_base_url } from '../config';

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

export function useFolders() {
	const { data: folders, isLoading, refetch } = useQuery(
		"folders",
		() => fetch(`${api_base_url}/folders/`).then((r) => r.json()),
		{
			staleTime: 30 * 1000,
		}
	);

	return { folders, isLoading, refetch};
}

export function useFolder(folder_id) {
	const { data: folder, isLoading, refetch, isError } = useQuery(
		["folder", folder_id],
		() => fetch(`${api_base_url}/folders/${folder_id}`).then((r) => r.json()),
		{
			//staleTime: 30 * 1000,
			refetchOnWindowFocus: false,
			refetchOnReconnect: false

		}
	);

	return { folder, isLoading, refetch, isError};
}

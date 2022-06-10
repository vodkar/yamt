import axios from "axios"

export function getNetworks(): string[] {
    return ['192.168.0.0/24', '192.168.48.0/24']
}

export function putNetworks(networks: string[]) {
    axios.put("http://127.0.0.1:8000/networks/", { networks: networks })
}
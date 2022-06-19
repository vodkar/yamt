import axios from "axios"

interface NetworksToScan {
    networks: string[]
}

interface NetworkResponse {
    data: NetworksToScan
}

export function getNetworks(callback: (networks: string[]) => void) {
    axios.get("http://127.0.0.1:8000/networks/").then(
        (resp: NetworkResponse) => { callback(resp.data.networks) }
    )
}

export function addNetworks(networks: string[], callback: (() => void)) {
    axios.post("http://127.0.0.1:8000/networks/", { networks: networks }).then(callback)
}
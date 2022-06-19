import axios from "axios"

interface ShortNetworkRelatedHost {
    id: string,
    ip: string
}

export type NetworkWithHosts = Map<string, ShortNetworkRelatedHost[]>

interface NetworkResponse {
    data?: object
}

export function getNetworks(callback: (networks: NetworkWithHosts) => void) {
    axios.get("http://127.0.0.1:8000/networks/").then(
        (resp: NetworkResponse) => {
            resp.data && callback(new Map(Object.entries(resp.data)));
            return resp
        }
    ).then(console.log)
}

export function addNetworks(networks: string[], callback: (() => void)) {
    axios.post("http://127.0.0.1:8000/networks/", { networks: networks }).then(callback)
}
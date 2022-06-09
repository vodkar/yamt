const axios = require('axios').default;

export interface Host {
    ip: string;
    name: string;
}

export type THostList = Host[]

interface HostResponse {
    data: THostList
}


export function fetchHosts(callback: (hosts: THostList) => void) {
    axios.get("http://127.0.0.1:8000/hosts/").then(
        (response: HostResponse) => { callback(response.data) }
    )
};

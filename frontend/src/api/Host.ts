const axios = require('axios').default;

interface ModelWithUUID {
    id: string;

}


export interface IPInterface extends ModelWithUUID {
    ip: string;
}

export interface NetworkCard extends ModelWithUUID {
    mac: string;
    interfaces: IPInterface[]
}

export interface Host extends ModelWithUUID, PatchDTOHost {
    name: string;
    cards: NetworkCard[]
}
export interface PatchDTOHost {
    name?: string;
}


export type THostList = Host[]

interface HostResponse {
    data: THostList
}

interface PatchHostResponse {
    data: Host
}


export function fetchHosts(callback: (hosts: THostList) => void) {
    axios.get("http://127.0.0.1:8000/hosts/").then(
        (response: HostResponse) => { callback(response.data) }
    )
};

export function updateHost(id: string, dto: PatchDTOHost, callback?: (host: Host) => void) {
    axios.patch(`http://127.0.0.1:8000/hosts/${id}`, dto).then(
        (response: PatchHostResponse) => { callback && callback(response.data) }
    )
}
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
export interface Host extends ModelWithUUID {
    name: string;
    cards: NetworkCard[]
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

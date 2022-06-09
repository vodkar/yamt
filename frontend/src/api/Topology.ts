import axios from "axios";
import { IPInterface } from "./Host"

interface IPInterfaceConnection {
    origin: IPInterface;
    destination: IPInterface
}

export interface ITopology {
    interface_connections: IPInterfaceConnection[]
}
interface TopologyResponse {
    data: ITopology
}



export function fetchTopology(callback: (topology: ITopology) => void) {
    axios.get("http://127.0.0.1:8000/topology/").then(
        (response: TopologyResponse) => { callback(response.data) }
    )
};

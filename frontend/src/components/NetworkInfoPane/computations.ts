import { NetworkWithHosts } from "../../api/Network";
import { INetworkGeneralInfoProps } from "./NetworkGeneralInfo";

export function getGeneralPropsFromMap(networks: NetworkWithHosts): INetworkGeneralInfoProps {
    let totalHosts = 0, totalNetworks = 0
    networks.forEach((v, k) => {
        totalNetworks += 1;
        v.forEach(host => {
            totalHosts += 1;
        })
    }
    )
    return { totalHosts, totalNetworks }
}
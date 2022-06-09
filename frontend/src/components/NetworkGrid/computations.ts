import { Host } from "../../api/Host";

export function getHostByInterfaceId(hosts: Host[], interface_id: string): Host | null {
    for (const host of hosts) {
        for (const card of host.cards) {
            for (const inter of card.interfaces) {
                if (inter.id == interface_id) {
                    return host
                }
            }
        }
    }
    return null
}
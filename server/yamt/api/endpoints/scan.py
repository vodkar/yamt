from fastapi import APIRouter, BackgroundTasks

from yamt.api.schemas.scan import NetworksToScan
from yamt.hosts import get_host_storage
from yamt.hosts.models.host import Host
from yamt.hosts.services import get_scanner


async def scan_and_save_networks(networks: NetworksToScan):
    scanner = get_scanner()
    hosts: list[Host] = []
    for network in networks.networks:
        async for host in scanner.scan_network(network):
            hosts.append(host)

    host_storage = get_host_storage()
    host_storage.add_hosts(hosts)


scan_router = APIRouter()


@scan_router.put("/")
def scan_network(tasks: BackgroundTasks, networks_to_scan: NetworksToScan):
    tasks.add_task(scan_and_save_networks, networks_to_scan)
    return {"message": "Scan is launched"}

from fastapi import APIRouter, BackgroundTasks

from yamt.api.schemas.scan import NetworksToScan
from yamt.common.helpers import get_logger
from yamt.hosts import get_host_storage, get_topology_builder
from yamt.hosts.models.host import Host
from yamt.hosts.services import get_scanner

_networks: NetworksToScan = NetworksToScan(networks=[])


def scan_and_save_networks(networks: NetworksToScan):
    logger = get_logger(__name__)
    scanner = get_scanner()
    hosts: list[Host] = []
    global _networks
    _networks = networks
    for network in networks.networks:
        for host in scanner.scan_network(network):
            logger.fatal(f"Scanned {network}, found: {host.dict()}")
            hosts.append(host)

    host_storage = get_host_storage()
    host_storage.add_hosts(hosts)

    topology_builder = get_topology_builder()
    topology_builder.build_topology(host_storage.get_interfaces())


scan_router = APIRouter()


@scan_router.get("/")
def get_networks() -> NetworksToScan:
    return _networks


@scan_router.put("/")
def scan_network(tasks: BackgroundTasks, networks_to_scan: NetworksToScan):
    tasks.add_task(scan_and_save_networks, networks_to_scan)
    return {"message": "Scan is launched"}

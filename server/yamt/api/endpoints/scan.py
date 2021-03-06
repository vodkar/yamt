from ipaddress import IPv6Network

from fastapi import APIRouter, BackgroundTasks
from pydantic import IPvAnyNetwork

from yamt.api.schemas.scan import PostNetworksSchema, ShortNetworkRelatedHost
from yamt.common.helpers import get_logger
from yamt.hosts import get_host_storage, get_network_storage, get_topology_builder
from yamt.hosts.models.host import Host
from yamt.hosts.network_storage import NetworkStorage
from yamt.hosts.services import get_scanner

network_storage: NetworkStorage = get_network_storage()


def scan_and_save_networks(networks: PostNetworksSchema):
    logger = get_logger(__name__)
    scanner = get_scanner()
    hosts: list[Host] = []
    network_storage.add_networks(networks.networks)
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
def get_networks() -> dict[IPvAnyNetwork, list[ShortNetworkRelatedHost]]:
    networks = get_host_storage().get_by_networks(network_storage.get_networks())
    return {
        network: [ShortNetworkRelatedHost(id=h.id, ip=ip) for ip, h in hosts.items()]
        for network, hosts in networks.items()
    }


@scan_router.post("/")
def scan_network(tasks: BackgroundTasks, networks_to_scan: PostNetworksSchema):
    if any(isinstance(network, IPv6Network) for network in networks_to_scan.networks):
        raise ValueError("IPv6 сети пока не поддерживаются")
    tasks.add_task(scan_and_save_networks, networks_to_scan)
    return {"message": "Scan is launched"}

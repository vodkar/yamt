from fastapi import APIRouter

from yamt.hosts import get_host_storage, get_network_storage
from yamt.hosts.models import Connection, Topology

topology_router = APIRouter()


@topology_router.get("/")
def get_topology() -> Topology:
    network_storage = get_network_storage()
    return network_storage.get_topology()

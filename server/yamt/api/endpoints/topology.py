from fastapi import APIRouter

from yamt.hosts import get_topology_builder
from yamt.hosts.models import Topology

topology_router = APIRouter()


@topology_router.get("/")
def get_topology() -> Topology:
    topology_builder = get_topology_builder()
    return topology_builder.get_current_topology()

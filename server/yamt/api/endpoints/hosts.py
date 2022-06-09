from fastapi import APIRouter

from yamt.hosts import get_host_storage
from yamt.hosts.models.host import Host

host_router = APIRouter()


@host_router.get("/")
def get_hosts() -> list[Host]:
    storage = get_host_storage()
    return list(storage.get_hosts())

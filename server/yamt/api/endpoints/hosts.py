from uuid import UUID

from fastapi import APIRouter

from yamt.hosts import PatchHostDTO, get_host_storage
from yamt.hosts.models.host import Host

host_router = APIRouter()


@host_router.get("/")
def get_hosts() -> list[Host]:
    storage = get_host_storage()
    return list(storage.get_hosts())


@host_router.patch("/{host_id}")
def patch_host(host_id: UUID, dto: PatchHostDTO) -> Host:
    storage = get_host_storage()
    return storage.update_host_data(host_id, dto)

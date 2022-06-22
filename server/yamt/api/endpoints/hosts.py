from itertools import chain
from uuid import UUID

from fastapi import APIRouter, HTTPException

from yamt.api.schemas.available_services import AvailableServices
from yamt.api.schemas.host import ExtendedHost
from yamt.hosts import PatchHostDTO, get_host_storage
from yamt.hosts.models.host import Host
from yamt.tcp_services.scanner import get_tcp_scanner
from yamt.tcp_services.services.ssh import get_ssh_storage

host_router = APIRouter()


@host_router.get("/")
def get_hosts() -> list[Host]:
    storage = get_host_storage()
    return list(storage.get_hosts())


@host_router.get("/{host_id}")
async def get_host(host_id: UUID):
    storage = get_host_storage()
    if not (host := storage.get_host(host_id)):
        raise HTTPException(status_code=404, detail="Host not found")
    ssh_storage = get_ssh_storage()
    tcp_port_scanner = get_tcp_scanner()
    ports = list(
        chain.from_iterable(ports for _, ports in tcp_port_scanner.scan_ports(host.iterate_over_ips(), [22]))
    )
    ExtendedHost(
        ssh_creds=ssh_storage.get_creds(host),
        available_services=AvailableServices.from_ports(ports),
        **host.dict(),
    )


@host_router.patch("/{host_id}")
def patch_host(host_id: UUID, dto: PatchHostDTO) -> Host:
    storage = get_host_storage()
    return storage.update_host_data(host_id, dto)

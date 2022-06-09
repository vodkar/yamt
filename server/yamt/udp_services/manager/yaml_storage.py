from typing import Any

from yamt.hosts.models.host import Host

from .storage import UDPServicesStorage


class YAMLUDPServicesStorage(UDPServicesStorage):
    def add_host_service(self, host: Host, service: str, data: dict[str, Any]):
        pass

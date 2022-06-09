from abc import ABC, abstractmethod
from typing import Any

from yamt.hosts import Host


class UDPServicesStorage(ABC):
    @abstractmethod
    def add_host_service(self, host: Host, service: str, data: dict[str, Any]):
        pass

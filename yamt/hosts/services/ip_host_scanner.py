from abc import ABC, abstractmethod
from ipaddress import IPv4Network
from typing import AsyncGenerator

from ..models import Host


class IPHostScanner(ABC):
    @abstractmethod
    async def scan_network(self, network: IPv4Network) -> AsyncGenerator[Host, None]:
        pass

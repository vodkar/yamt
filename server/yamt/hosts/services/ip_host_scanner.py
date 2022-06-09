from abc import ABC, abstractmethod
from ipaddress import IPv4Network
from typing import AsyncIterator

from ..models import Host


class IPHostScanner(ABC):
    @abstractmethod
    async def scan_network(self, network: IPv4Network) -> AsyncIterator[Host]:
        # mypy hack
        if False:
            yield Host()

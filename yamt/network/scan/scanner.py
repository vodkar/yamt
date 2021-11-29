from abc import ABC, abstractmethod
from ipaddress import IPv4Network
from typing import AsyncGenerator

from yamt.hosts.host import Host


class Scanner(ABC):
    @abstractmethod
    async def scan_network(self, network: IPv4Network) -> AsyncGenerator[Host, None]:
        pass

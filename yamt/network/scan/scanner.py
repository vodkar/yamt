from abc import ABC, abstractmethod
from ipaddress import IPv4Network


class Scanner(ABC):
    @abstractmethod
    async def scan_network(self, network: IPv4Network):
        pass

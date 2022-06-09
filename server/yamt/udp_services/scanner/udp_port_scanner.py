from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from typing import AsyncGenerator, Iterable

from yamt.hosts import Host


class UDPPortScanner(ABC):
    @abstractmethod
    async def scan_host(
        self, hosts: Iterable[Host], ports: list[int]
    ) -> AsyncGenerator[tuple[IPv4Address, list[int]], None]:
        pass

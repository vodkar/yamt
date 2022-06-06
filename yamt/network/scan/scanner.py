from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from typing import AsyncGenerator, Iterable


class PortScanner(ABC):
    @abstractmethod
    async def scan_ports(
        self, ips: Iterable[IPv4Address], port_nums: Iterable[int]
    ) -> AsyncGenerator[tuple[IPv4Address, dict[int, list[str]]], None]:
        pass

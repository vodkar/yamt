from abc import ABC, abstractmethod
from ipaddress import IPv4Address, IPv4Network
from typing import AsyncGenerator, Iterable

from yamt.hosts.host import Host


class DeviceScanner(ABC):
    @abstractmethod
    async def scan_network(self, network: IPv4Network) -> AsyncGenerator[Host, None]:
        pass


class PortScanner(ABC):
    @abstractmethod
    async def scan_ports(
        self, ips: Iterable[IPv4Address], port_nums: Iterable[int]
    ) -> AsyncGenerator[tuple[IPv4Address, dict[int, list[str]]], None]:
        pass

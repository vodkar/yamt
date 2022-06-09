from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from typing import AsyncGenerator, AsyncIterable, Iterable


class TCPPortScanner(ABC):
    @abstractmethod
    async def scan_ports(
        self, ips: AsyncIterable[IPv4Address] | IPv4Address, port_nums: Iterable[int]
    ) -> AsyncGenerator[tuple[IPv4Address, list[int]], None]:
        if False:
            yield IPv4Address(""), [1]

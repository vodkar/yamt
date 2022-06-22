from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from typing import Generator, Iterable


class TCPPortScanner(ABC):
    @abstractmethod
    def scan_ports(
        self, ips: Iterable[IPv4Address] | IPv4Address, port_nums: Iterable[int]
    ) -> Generator[tuple[IPv4Address, list[int]], None, None]:
        if False:
            yield IPv4Address(""), [1]

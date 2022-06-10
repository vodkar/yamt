from abc import ABC, abstractmethod
from ipaddress import IPv4Network
from typing import Iterator

from ..models import Host


class IPHostScanner(ABC):
    @abstractmethod
    def scan_network(self, network: IPv4Network) -> Iterator[Host]:
        # mypy hack
        if False:
            yield Host()

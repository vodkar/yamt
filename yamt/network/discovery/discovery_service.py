from ipaddress import IPv4Network
from typing import List

from yamt.common.helpers import get_logger, timeit
from yamt.hosts import Host

from ..scan import DeviceScanner


class DiscoveryService:

    logger = get_logger(__name__)

    def __init__(self, scanner: DeviceScanner) -> None:
        self.scanner = scanner

    @timeit(logger)
    async def discover_network(self, network: IPv4Network):
        return self.scanner.scan_network(network)

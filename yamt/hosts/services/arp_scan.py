from ipaddress import IPv4Network
from typing import AsyncGenerator

import scapy.all as scapy

from yamt.hosts import Host

from .ip_host_scanner import IPHostScanner


class ARPScanner(IPHostScanner):
    timeout: int

    def __init__(self, timeout: int=3) -> None:
        self.timeout = timeout
        super().__init__()

    async def scan_network(self, network: IPv4Network) -> AsyncGenerator[Host, None]:
        frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=str(network))
        results, _ = scapy.srp(frame, timeout=self.timeout, verbose=False)
        for _, recieved in results:
            yield Host(ip=recieved.payload.psrc, mac=recieved.src, name="")

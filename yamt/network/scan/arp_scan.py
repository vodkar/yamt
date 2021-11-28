from ipaddress import IPv4Network
from typing import List

import scapy.all as scapy

from yamt.hosts import Host

from .scanner import Scanner


class ARPScanner(Scanner):
    timeout: int

    def __init__(self, timeout=3) -> None:
        self.timeout = timeout
        super().__init__()

    async def scan_network(self, network: IPv4Network) -> List[Host]:
        frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=str(network))
        results, _ = scapy.srp(frame, timeout=self.timeout)
        return [Host(ip=recieved.payload.psrc, mac=recieved.src, name="") for sent, recieved in results]

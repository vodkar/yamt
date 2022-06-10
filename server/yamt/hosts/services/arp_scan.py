from ipaddress import IPv4Address, IPv4Network
from tabnanny import verbose
from typing import AsyncIterator, Iterable, Iterator

import scapy.all as scapy

from yamt.hosts import Host

from .ip_host_scanner import IPHostScanner


class ARPScanner(IPHostScanner):
    timeout: int

    def __init__(self, current_network: IPv4Network, timeout: int = 3) -> None:
        self.timeout = timeout
        self._current_network = current_network
        super().__init__()

    def scan_network(self, network: IPv4Network) -> Iterator[Host]:
        if network.subnet_of(self._current_network):
            frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=str(network))
            results, _ = scapy.srp(frame, timeout=self.timeout, verbose=False)
            for _, recieved in results:
                yield Host.create_simple_host(ip=recieved.payload.psrc, mac=recieved.src, name="")
        else:
            for host in self._ping_scan(network):
                yield host

    def _ping_scan(self, network: IPv4Network) -> Iterator[Host]:
        for address in network:
            frame = scapy.IP(dst=str(address), ttl=10) / scapy.ICMP()
            if result := scapy.sr1(frame, timeout=self.timeout, verbose=False):
                yield Host.create_simple_host(ip=result.dst)

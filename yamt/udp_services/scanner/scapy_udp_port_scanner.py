from ipaddress import IPv4Address
from typing import AsyncGenerator, Iterable

import scapy

from yamt.hosts import Host

from .udp_port_scanner import UDPPortScanner


class ScapyUDPPortScanner(UDPPortScanner):
    def __init__(self, timeout: int=3, verbose_mode: bool = False) -> None:
        self.timeout =timeout
        self._verbose_mode = verbose_mode
        super().__init__()
    async def scan_host(
        self, hosts: Iterable[Host], ports: list[int]
    ) -> AsyncGenerator[tuple[IPv4Address, list[int]], None]:
        for host in hosts:
            frame = scapy.IP(dst=host.ip) / scapy.UDP(dport=ports)
            open_ports: list[int] = []
            for result in scapy.sr(frame, timeout=self.timeout, verbose=self._verbose_mode):
                if not result and (
                    result.haslayer(scapy.ICMP)
                    and (icmp := result.getlayer(scapy.ICMP))
                    and icmp.type != 3
                ):
                    open_ports.append(1)
                    
            yield host.ip, open_ports

        

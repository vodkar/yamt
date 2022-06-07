from ipaddress import IPv4Address
from typing import AsyncGenerator, AsyncIterable, Iterable

import scapy.all as scapy

from .scanner import PortScanner


class TCPStealthUdpPortScanner(PortScanner):
    def __init__(self, timeout: int = 3):
        self._timeout = timeout

    async def scan_ports(
        self, ips: AsyncIterable[IPv4Address], port_nums: Iterable[int]
    ) -> AsyncGenerator[tuple[IPv4Address, list[int]], None]:
        sport = scapy.RandShort()
        async for ip in ips:
            opened_ports: list[int] = []
            for port in port_nums:
                syn_on_ips = scapy.IP(dst=str(ip)) / scapy.TCP(sport=sport, dport=port, flags="S")
                result = scapy.sr(syn_on_ips, timeout=self._timeout)
                if result and result.haslayer(TCP) and result.getlayer(TCP).flags == 0x12:
                    scapy.sr(
                        scapy.IP(dst=str(ip)) / scapy.TCP(sport=sport, dport=port, flags="S"), timeout=self._timeout
                    )
                    opened_ports.append(port)
            yield ip, opened_ports

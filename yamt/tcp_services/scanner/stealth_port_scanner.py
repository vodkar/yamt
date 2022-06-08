from ipaddress import IPv4Address
from typing import AsyncGenerator, AsyncIterable, Iterable

import scapy.all as scapy

from .tcp_port_scanner import TCPPortScanner


class TCPStealthPortScanner(TCPPortScanner):
    def __init__(self, timeout: int = 3):
        self._timeout = timeout

    async def scan_ports(
        self, ips: AsyncIterable[IPv4Address] | IPv4Address, port_nums: Iterable[int]
    ) -> AsyncGenerator[tuple[IPv4Address, list[int]], None]:
        port_nums = list(port_nums)
        if isinstance(ips, IPv4Address):
            yield self._scan(ips, port_nums)
        else:
            async for ip in ips:
                yield self._scan(ip, port_nums)

    def _scan(self, ip: IPv4Address, port_nums: list[int]):
        opened_ports: list[int] = []
        sport = scapy.RandShort()
        for port in port_nums:
            syn_on_ips = scapy.IP(dst=str(ip)) / scapy.TCP(sport=sport, dport=port, flags="S")
            result = scapy.sr1(syn_on_ips, timeout=self._timeout, verbose=False)
            if result and result.haslayer(scapy.TCP) and result.getlayer(scapy.TCP).flags == 0x12:
                scapy.sr(
                    scapy.IP(dst=str(ip)) / scapy.TCP(sport=sport, dport=port, flags="S"),
                    timeout=self._timeout,
                    verbose=False,
                )
                opened_ports.append(port)
        return ip, opened_ports

from functools import reduce
from ipaddress import IPv4Address
from operator import truediv
from typing import AsyncGenerator, Iterable

import scapy.all as scapy

from .scanner import PortScanner


class TCPStealthUdpPortScanner(PortScanner):
    async def scan_ports(
        self, ips: Iterable[IPv4Address], port_nums: Iterable[int]
    ) -> AsyncGenerator[tuple[IPv4Address, dict[int, list[str]]], None]:
        sport = scapy.RandShort()
        port_nums = list(port_nums)
        syn_on_ports = scapy.TCP(sport=sport, dport=port_nums, flags="S")
        syn_on_ips = scapy.IP(dst=list(map(str, ips))) / syn_on_ports
        scapy.IP(dst="192.168.221.128", flags=2) / scapy.TCP(
            sport=sport,
            dport=631,
            flags="S",
            options=[
                ("MSS", 0xFFD7),
                ("SAckOK", b""),
                ("Timestamp", (0x02180683, 0)),
                ("NOP", None),
                ("WScale", 7),
            ],
            window=65495,
        ) / scapy.Ether(dst="00:00:00:00:00:00")
        for result in scapy.sr(syn_on_ips, timeout=3):
            if not result or (
                result.haslayer(scapy.ICMP)
                and (icmp := result.getlayer(scapy.ICMP))
                and icmp.type == 3
                and icmp.code in [1, 2, 3, 9, 10, 13]
            ):
                yield None, None
            else:
                flags = result.get_layer(TCP).flags
                if flags == 0x12:
                    scapy.sr
                    yield None, "tcp"
                elif flags == 0x14:
                    yield None, None
                else:
                    raise Exception("Unknown answer!")

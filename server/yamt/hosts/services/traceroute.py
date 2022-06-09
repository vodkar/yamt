from ipaddress import IPv4Address
from typing import Generator, Iterable

from scapy import all as scapy


def traceroute(ips: Iterable[IPv4Address]) -> Generator[list[IPv4Address], None, None]:
    for ip in ips:
        yield _traceroute(ip)


def _traceroute(ip: IPv4Address) -> list[IPv4Address]:
    ans, _ = scapy.sr(IP(dst=str(ip), ttl=(4, 25), id=scapy.RandShort()) / scapy.TCP(flags=0x2))
    return [IPv4Address(rcv.src) for _, rcv in ans]

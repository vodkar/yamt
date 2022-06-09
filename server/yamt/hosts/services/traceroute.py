from tabnanny import verbose
from typing import Generator, Iterable

from pydantic import IPvAnyAddress
from scapy import all as scapy


def traceroute(ips: Iterable[IPvAnyAddress]) -> Generator[list[IPvAnyAddress], None, None]:
    for ip in ips:
        yield _traceroute(ip)[::-1]


def _traceroute(ip: IPvAnyAddress) -> list[IPvAnyAddress]:
    ans, _ = scapy.traceroute(str(ip), verbose=False, maxttl=20)
    return [IPvAnyAddress(rcv.dst) for _, rcv in ans] + [ip]

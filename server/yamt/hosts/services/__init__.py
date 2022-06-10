from ipaddress import IPv4Network

from .arp_scan import ARPScanner  # type: ignore
from .ip_host_scanner import IPHostScanner  # type: ignore
from .topology_builder import TopologyBuilder  # type: ignore


def get_scanner() -> IPHostScanner:
    return ARPScanner(IPv4Network("192.168.0.0/24"))

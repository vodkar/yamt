from .arp_scan import ARPScanner  # type: ignore
from .ip_host_scanner import IPHostScanner  # type: ignore
from .topology_builder import TopologyBuilder


def get_scanner() -> IPHostScanner:
    return ARPScanner()

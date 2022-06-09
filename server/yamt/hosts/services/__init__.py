from .arp_scan import ARPScanner  # type: ignore
from .ip_host_scanner import IPHostScanner  # type: ignore


def get_scanner() -> IPHostScanner:
    return ARPScanner()

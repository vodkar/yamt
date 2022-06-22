from functools import cache

from .stealth_port_scanner import TCPStealthPortScanner
from .tcp_port_scanner import TCPPortScanner


@cache
def get_tcp_scanner() -> TCPPortScanner:
    return TCPStealthPortScanner()

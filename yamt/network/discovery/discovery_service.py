from ipaddress import IPv4Network
from typing import List

from scapy.all import 

from hosts import Host
from common.helpers import timeit,get_logger


class DiscoveryService:

    logger = get_logger(__name__)

    @timeit(logger)
    def discover_network(self, network: IPv4Network) -> List[Host]:


    def arp_scan(network, ports):

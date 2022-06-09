from functools import cache

from .host_group_storage import HostGroupStorage  # type: ignore
from .host_storage import HostStorage  # type: ignore
from .models import Host, HostGroup, MacAddress  # type: ignore
from .models.mac_address import MacAddress  # type: ignore
from .services import TopologyBuilder  # type: ignore


@cache
def get_host_storage():
    return HostStorage("hosts.yaml")

@cache
def get_topology_builder():
    return TopologyBuilder(get_host_storage())

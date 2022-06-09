from functools import cache

from .host_group_storage import HostGroupStorage  # type: ignore
from .host_storage import HostStorage  # type: ignore
from .models import Host, HostGroup, MacAddress  # type: ignore
from .models.mac_address import MacAddress  # type: ignore


@cache
def get_host_storage():
    return HostStorage("hosts.yaml")

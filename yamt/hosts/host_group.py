from common.model import YamtModel

from .host import Host


class HostGroup(YamtModel):
    name: str
    hosts: list[Host]

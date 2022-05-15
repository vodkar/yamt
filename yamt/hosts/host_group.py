from common.model import YamtModel

from .host import Host


class HostGroup(YamtModel):
    name: str
    __hosts: list[Host]

    def add_host(self, host: Host):
        pass

    def remove_host(self, host: Host):
        pass

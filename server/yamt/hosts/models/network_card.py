from pydantic import IPvAnyAddress

from yamt.common.model import YamtModelWithId

from .ip_interface import IPInterface
from .mac_address import MacAddress


class NetworkCard(YamtModelWithId):
    mac: MacAddress
    interfaces: list[IPInterface]

    def get_interface_by_ip(self, ip: IPvAnyAddress) -> IPInterface | None:
        if card := [interface for interface in self.interfaces if ip == interface.ip]:
            return card[0]
        return None

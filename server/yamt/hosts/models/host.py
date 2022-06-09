from __future__ import annotations

from pydantic import IPvAnyAddress

from yamt.common.model import YamtModelWithId
from yamt.hosts.models.ip_interface import IPInterface
from yamt.hosts.models.mac_address import MacAddress

from .network_card import NetworkCard


class Host(YamtModelWithId):
    name: str
    cards: list[NetworkCard]

    @classmethod
    def create_simple_host(cls, ip: IPvAnyAddress | str, mac: MacAddress | str, name: str = "") -> Host:
        return cls(name=name, cards=[NetworkCard(mac=MacAddress(mac), interfaces=[IPInterface(ip=ip)])])

from __future__ import annotations

from uuid import UUID

from pydantic import IPvAnyAddress

from yamt.common.model import YamtModelWithId
from yamt.hosts.models.ip_interface import IPInterface
from yamt.hosts.models.mac_address import MacAddress

from .network_card import NetworkCard


class Host(YamtModelWithId):
    name: str
    cards: list[NetworkCard]

    @classmethod
    def create_simple_host(cls, ip: IPvAnyAddress | str, mac: MacAddress | str | None = None, name: str = "") -> Host:
        return cls(name=name, cards=[NetworkCard(mac=mac, interfaces=[IPInterface(ip=ip)])])

    def get_card_by_mac(self, mac: MacAddress) -> NetworkCard | None:
        if card := [card for card in self.cards if mac == card.mac]:
            return card[0]
        return None

    def get_card_by_id(self, id: UUID) -> NetworkCard | None:
        if card := [card for card in self.cards if id == card.id]:
            return card[0]
        return None

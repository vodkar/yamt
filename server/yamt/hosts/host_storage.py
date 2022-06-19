from collections import defaultdict
from contextlib import contextmanager
from ipaddress import IPv4Address
from pathlib import Path
from typing import Any, Generator, Iterable
from uuid import UUID

import yaml
from pydantic import IPvAnyAddress, IPvAnyNetwork

from yamt.common.helpers import get_logger
from yamt.hosts.models.host import PatchHostDTO
from yamt.hosts.models.ip_interface import IPInterface
from yamt.hosts.models.mac_address import MacAddress
from yamt.hosts.models.network_card import NetworkCard

from .models import Host


class HostStorage:
    def __init__(self, yaml_path: str):
        self._yaml_path: str = yaml_path
        self._cached = False
        self._logger = get_logger(__name__, prefix="HostStorage")
        self._hosts: list[Host] = []
        self._interfaces: list[IPInterface] = []

        list(self.get_hosts())

    def get_hosts(self) -> Generator[Host, None, None]:
        if not self._cached:
            self._hosts = []
            self._interfaces = []
            self._logger.debug("get_hosts not cached, retrieve hosts from file")
            with self._open_yaml() as data:
                for host in data.get("hosts", []):
                    self._logger.debug(f"Found host: {host}")
                    self._hosts.append(Host(**host))
                for inter in data.get("interfaces", []):
                    self._logger.debug(f"Found interface: {inter}")
                    self._interfaces.append(IPInterface(**inter))
            self._cached = True

        yield from self._hosts

    def add_hosts(self, hosts: list[Host]) -> None:
        for host in hosts:
            if self.get_host(host.id):
                continue
            if hosts_with_same_macs := [
                (same_host, card.mac) for card in host.cards if (same_host := self.get_host_by_mac(card.mac))
            ]:
                for same_host, mac in hosts_with_same_macs:
                    if (same_card := same_host.get_card_by_mac(mac)) and (
                        host_card := host.get_card_by_mac(mac)
                    ):
                        for interface in host_card.interfaces:
                            self.add_interface_to_host_card(same_host.id, same_card.id, interface)
                continue
            self._logger.debug(f"Added host: {host.json()}")
            self._hosts.append(host)
        self._save()

    def get_host(self, id: UUID) -> Host | None:
        for host in self._hosts:
            if host.id == id:
                return host
        return None

    def get_host_by_mac(self, mac: MacAddress) -> Host | None:
        for host in self._hosts:
            if any(mac == card.mac for card in host.cards):
                return host
        return None

    def add_network_card_to_host(self, host_id: UUID, card: NetworkCard):
        if host := self.get_host(host_id):
            if host.get_card_by_mac(card.mac):
                return
            host.cards.append(card)
            self._save()
        else:
            raise ValueError("Host not found!")

    def add_interface_to_host_card(self, host_id: UUID, card_id: UUID, interface: IPInterface):
        if (host := self.get_host(host_id)) and (card := host.get_card_by_id(card_id)):
            if card.get_interface_by_ip(interface.ip):
                return
            card.interfaces.append(interface)
            self._save()
        else:
            raise ValueError("Host and card not found!")

    def get_interfaces(self) -> Iterable[IPInterface]:
        for interface in self._interfaces:
            yield interface
        for host in self._hosts:
            for card in host.cards:
                for interface in card.interfaces:
                    yield interface

    def get_interface(self, ip: IPvAnyAddress) -> IPInterface | None:
        for interface in self.get_interfaces():
            if interface.ip == ip:
                return interface
        return None

    def update_host_data(self, id: UUID, dto: PatchHostDTO) -> Host:
        if host := self.get_host(id):
            for key, item in dto.dict().items():
                setattr(host, key, item)
            self._save()
            return host
        else:
            raise ValueError(f"Не удалось найти хост с идентификатором {id}")

    def add_interfaces(self, interfaces: Iterable[IPInterface]):
        self._interfaces.extend(interfaces)
        self._save()

    def get_by_networks(self, networks: Iterable[IPvAnyNetwork]) -> dict[IPvAnyNetwork, dict[IPvAnyAddress, Host]]:
        d: dict[IPvAnyNetwork, dict[IPvAnyAddress, Host]] = {network: {} for network in networks}

        for host in self._hosts:
            for card in host.cards:
                for interface in card.interfaces:
                    for network in d.keys():
                        if interface.ip in network:
                            d[network][interface.ip] = host
                            continue

        return d

    def _save(self):
        with open(self._yaml_path, "w") as f:
            yaml.dump(
                {
                    "hosts": [host.dict() for host in self._hosts],
                    "interfaces": [inter.dict() for inter in self._interfaces],
                },
                f,
                yaml.Dumper,
            )

    @contextmanager
    def _open_yaml(self) -> Generator[dict[str, list[dict[str, Any]]], None, None]:
        try:
            with open(self._yaml_path, "r") as f:
                yield yaml.load(f, Loader=yaml.Loader) or {}
        except FileNotFoundError:
            Path(self._yaml_path).touch()
            with open(self._yaml_path, "r") as f:
                yield {}

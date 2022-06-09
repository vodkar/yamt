from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator, Iterable
from uuid import UUID

import yaml
from pydantic import IPvAnyAddress

from yamt.common.helpers import get_logger
from yamt.hosts.models.ip_interface import IPInterface

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
                for host in data["hosts"]:
                    self._logger.debug(f"Found host: {host}")
                    self._hosts.append(Host(**host))
                for inter in data["interfaces"]:
                    self._logger.debug(f"Found interface: {inter}")
                    self._interfaces.append(IPInterface(**inter))
            self._cached = True

        yield from self._hosts

    def add_hosts(self, hosts: list[Host]) -> None:
        for host in hosts:
            if host in self._hosts:
                continue
            self._logger.debug(f"Added host: {host.json()}")
            self._hosts.append(host)
        self._save()

    def get_host(self, id: UUID) -> Host | None:
        for host in self._hosts:
            if host.id == id:
                return host
        return None

    def get_interface(self, ip: IPvAnyAddress) -> IPInterface | None:
        for interface in self._interfaces:
            if interface.ip == ip:
                return interface
        for host in self._hosts:
            for card in host.cards:
                for interface in card.interfaces:
                    if interface.ip == ip:
                        return interface
        return None

    def add_interfaces(self, interfaces: Iterable[IPInterface]):
        self._interfaces.extend(interfaces)
        self._save()

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

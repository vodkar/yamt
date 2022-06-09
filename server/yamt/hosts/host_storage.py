from contextlib import contextmanager
from ipaddress import IPv4Address
from pathlib import Path
from typing import Any, Generator

import yaml

from yamt.common.helpers import get_logger

from .models import Host


class HostStorage:
    def __init__(self, yaml_path: str):
        self._yaml_path: str = yaml_path
        self._cached = False
        self._logger = get_logger(__name__, prefix="HostStorage")
        self._hosts: list[Host] = []
        
        list(self.get_hosts())

    def get_hosts(self) -> Generator[Host, None, None]:
        if not self._cached:
            self._hosts = []
            self._logger.debug("get_hosts not cached, retrieve hosts from file")
            with self._open_yaml() as data:
                for host in data:
                    self._logger.debug(f"Found host: {host}")
                    self._hosts.append(Host(**host))
            self._cached = True

        yield from self._hosts

    def add_hosts(self, hosts: list[Host]) -> None:
        for host in hosts:
            self._logger.debug(f"Added host: {host.json()}")
            self._hosts.append(host)
        self._save()

    def get_host(self, ip: IPv4Address) -> Host | None:
        for host in self._hosts:
            if host.ip == ip:
                return host
        return None

    def _save(self):
        with open(self._yaml_path, "w") as f:
            yaml.dump([host.dict() for host in self._hosts], f, yaml.Dumper)

    @contextmanager
    def _open_yaml(self) -> Generator[list[dict[str, Any]], None, None]:
        try:
            with open(self._yaml_path, "r") as f:
                yield yaml.load(f, Loader=yaml.Loader) or []
        except FileNotFoundError:
            Path(self._yaml_path).touch()
            with open(self._yaml_path, "r") as f:
                yield []
            
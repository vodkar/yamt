from contextlib import contextmanager
from functools import cache
from ipaddress import IPv4Address
from typing import Any, Generator

import yaml

from yamt.common.helpers import get_logger
from yamt.hosts.host import Host


class HostStorage:
    def __init__(self, yaml_path: str):
        self._yaml_path: str = yaml_path
        self._hosts: list[Host] = []
        self._cached = False
        self._logger = get_logger(__name__, prefix="HostStorage")

    def get_hosts(self) -> Generator[Host, None, None]:
        if not self._cached:
            self._logger.debug("get_hosts not cached, retrieve hosts from file")
            with self._open_yaml() as data:
                for host in data:
                    self._logger.debug(f"Found host: {host}")
                    self._hosts.append(Host(**host))

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
            yaml.dump(self._hosts, f, yaml.Dumper)

    @contextmanager
    def _open_yaml(self) -> Generator[list[dict[str, Any]], None, None]:
        with open(self._yaml_path, "r") as f:
            yield yaml.load(f, Loader=yaml.Loader)

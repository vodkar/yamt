from contextlib import contextmanager
from typing import Any, Generator

import yaml

from yamt.common.helpers import get_logger
from yamt.hosts.host_group import HostGroup
from yamt.hosts.host_storage import HostStorage


class HostGroupStorage:
    def __init__(self, yaml_path: str, host_storage: HostStorage):
        self._yaml_path: str = yaml_path
        self._host_groups: list[HostGroup] = []
        self._cached = False
        self._host_storage = host_storage
        self._logger = get_logger(__name__, prefix="HostGroupStorage")

    def get_host_groups(self) -> Generator[HostGroup, None, None]:
        if not self._cached:
            self._logger.debug("get_host_groups not cached, retrieve groups from file")
            with self._open_yaml() as data:
                for host_group in data:
                    self._logger.debug(f"Found host group: {host_group}")
                    self._host_groups.append(
                        HostGroup(
                            name=host_group["name"],
                            hosts=[self._host_storage.get_host(host["ip"]) for host in host_group["hosts"]],
                        )
                    )

        yield from self._host_groups

    def add_host_groups(self, host_groups: list[HostGroup]) -> None:
        for host_group in host_groups:
            self._logger.debug(f"Added host group: {host_group.json()}")
            self._host_groups.append(host_group)
        self._save()

    def _save(self):
        with open(self._yaml_path, "w") as f:
            to_save: list[dict[str, Any]] = []
            for group in self._host_groups:
                to_save.append({"name": group.name, "hosts": [host.ip for host in group.hosts]})
            yaml.dump(to_save, f, yaml.Dumper)

    @contextmanager
    def _open_yaml(self) -> Generator[list[dict[str, Any]], None, None]:
        with open(self._yaml_path, "r") as f:
            yield yaml.load(f, Loader=yaml.Loader)

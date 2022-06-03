from contextlib import contextmanager
from typing import Any, Generator

import yaml

from yamt.hosts.host import Host


class HostStorage:
    def __init__(self, yaml_path: str):
        self._yaml_path: str = yaml_path

    def get_hosts(self) -> Generator[Host, None, None]:
        with self._open_yaml() as data:
            for host in data["hosts"]:
                yield Host(**host)

    def save_hosts(self) -> Generator[Host, None, None]:
        with self._open_yaml() as data:
            for host in data["hosts"]:
                yield Host(**host)

    @contextmanager
    def _open_yaml(self) -> Generator[dict[str, Any], None, None]:
        with open(self._yaml_path, "r") as f:
            yield yaml.load(f, Loader=yaml.Loader)

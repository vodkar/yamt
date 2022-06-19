from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator, Iterable

import yaml
from pydantic import IPvAnyNetwork

from yamt.common.helpers import get_logger

from .models.topology import Topology


class NetworkStorage:
    def __init__(self, yaml_path: str):
        self._yaml_path: str = yaml_path
        self._logger = get_logger(__name__, prefix="NetworkStorage")
        self._topology: Topology
        self._networks: list[IPvAnyNetwork] = []

    def get_networks(self) -> Generator[IPvAnyNetwork, None, None]:
        self._logger.debug("Retrieve networks from file")
        self._networks = []
        with self._open_yaml() as data:
            for network in data.get("networks", []):
                if isinstance(network, IPvAnyNetwork):
                    self._logger.debug(f"Found network: {network}")
                    self._networks.append(network)
                else:
                    raise TypeError(f"network has type: {type(network)}. Expected: IPvAnyNetwork")

        yield from self._networks

    def get_topology(self):
        self._logger.debug("Retrieve topology from file")
        with self._open_yaml() as data:
            if topology := data.get("topology"):
                if isinstance(topology, dict):
                    self._logger.debug(f"Found topology: {topology}")
                    self._topology = Topology(**topology)
                else:
                    raise TypeError(f"topology has type: {type(topology)}. Expected: Topology")

    def add_networks(self, networks: Iterable[IPvAnyNetwork]):
        self._networks.extend(networks)
        self._save()

    def _save(self):
        with open(self._yaml_path, "w") as f:
            yaml.dump(
                {"networks": self._networks, "topology": self._topology or None},
                f,
                yaml.Dumper,
            )

    @contextmanager
    def _open_yaml(self) -> Generator[dict[str, list[dict[str, Any]] | dict[str, Any]], None, None]:
        try:
            with open(self._yaml_path, "r") as f:
                yield yaml.load(f, Loader=yaml.Loader) or {}
        except FileNotFoundError:
            Path(self._yaml_path).touch()
            with open(self._yaml_path, "r") as f:
                yield {}

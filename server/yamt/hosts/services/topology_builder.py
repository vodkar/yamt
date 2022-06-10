from typing import Iterable

from pydantic import IPvAnyAddress

from yamt.hosts.host_storage import HostStorage

from ..models import Connection, IPInterface, Topology
from .traceroute import traceroute


class TopologyBuilder:
    def __init__(self, host_storage: HostStorage) -> None:
        self._host_storage = host_storage
        self._topology: Topology | None = None

    def build_topology(self, interfaces: Iterable[IPInterface]) -> Topology:
        connections: list[Connection[IPInterface]] = []
        for routes in traceroute(interface.ip for interface in interfaces):
            for i in range(1, len(routes)):
                origin, dest = self.get_or_save_interface(routes[i - 1], routes[i])
                connections.append(Connection(origin=origin, destination=dest))
        if self._topology:
            connections.extend(self._topology.interface_connections)
        self._topology = Topology(interface_connections=connections)
        return self._topology

    def get_current_topology(self) -> Topology:
        if not self._topology:
            raise ValueError("Topology is not builded")
        return self._topology

    def get_or_save_interface(self, *ips: IPvAnyAddress) -> Iterable[IPInterface]:
        for ip in ips:
            if not (interface := self._host_storage.get_interface(ip)):
                interface = IPInterface(ip=ip)
                self._host_storage.add_interfaces([interface])
            yield interface

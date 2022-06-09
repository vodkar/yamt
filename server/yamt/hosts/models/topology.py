from typing import Generic, TypeVar

from yamt.common.model import YamtModel

from .host import Host
from .ip_interface import IPInterface

T = TypeVar("T")


class Connection(YamtModel, Generic[T]):
    origin: T
    destination: T


class Topology(YamtModel):
    interface_connections: list[Connection[IPInterface]]

    # def get_host_topology(self) -> Connection[Host]:
    #     pass

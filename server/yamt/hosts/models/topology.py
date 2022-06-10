from typing import Generic, TypeVar

from pydantic import validator

from yamt.common.model import YamtModel

from .host import Host
from .ip_interface import IPInterface

T = TypeVar("T", IPInterface, Host)


class Connection(YamtModel, Generic[T]):
    origin: T
    destination: T


class Topology(YamtModel):
    interface_connections: list[Connection[IPInterface]]

    @validator("interface_connections")
    def remove_duplicates(cls, v: list[Connection[IPInterface]]):
        visited: list[Connection[IPInterface]] = []
        for conn in v:
            if conn.origin.id != conn.destination.id and not any(
                (Topology.compare_connections(visit, conn)) for visit in visited
            ):
                visited.append(conn)

        return visited

    @staticmethod
    def compare_connections(left: Connection[T], right: Connection[T]) -> bool:
        if isinstance(left.origin, IPInterface) and isinstance(right.origin, IPInterface):
            return Topology.compare_ip_interface_connection(left, right)  # type: ignore

        raise NotImplementedError(f"Comparion for connection type '{type(left)}' is not implemented")

    @staticmethod
    def compare_ip_interface_connection(left: Connection[IPInterface], right: Connection[IPInterface]) -> bool:
        return (left.origin.ip == right.origin.ip and left.destination.ip == right.destination.ip) or (
            left.origin.ip == right.destination.ip and left.destination.ip == right.origin.ip
        )

    # def get_host_topology(self) -> Connection[Host]:
    #     pass

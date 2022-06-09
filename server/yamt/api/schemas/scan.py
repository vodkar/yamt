from ipaddress import IPv4Network

from pydantic import BaseModel


class NetworksToScan(BaseModel):
    networks: list[IPv4Network]

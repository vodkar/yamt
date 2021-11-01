from pydantic import BaseModel
from ipaddress import IPv4Address

class IpHost(BaseModel):
    ip: IPv4Address


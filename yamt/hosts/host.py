from ipaddress import IPv4Address

from yamt.common.model import YamtModel

from .mac_address import MacAddress


class Host(YamtModel):
    ip: IPv4Address
    mac: MacAddress
    name: str

    # @validator("mac")
    # def mac_vallidator(cls, v):
    #     if isinstance(v, MacAddress):
    #         return v
    #     if isinstance(v, str):
    #         return MacAddress(v)
    #     raise TypeError(f"Unknown type for 'mac' field: {type(v)}")

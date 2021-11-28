import re
from abc import ABC

from pydantic import validator

from yamt.common.model import YamtModel

_MAC_REGEX = re.compile(r"^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$")


class IHostIdentifier(ABC):
    pass


class MacAddress(YamtModel):
    mac: str

    def __init__(self, mac: str) -> None:
        super().__init__(mac=mac.strip())

    @validator("mac")
    def vaildate_mac(cls, v):
        if not re.search(_MAC_REGEX, v):
            raise ValueError(f"Unkown mac address format: {v}", cls)

import re
from abc import ABC

from pydantic import validator

from yamt.common.model import YamtModel

_MAC_REGEX = re.compile(r"^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$")


class IHostIdentifier(ABC):
    pass


class MacAddress(str):
    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def validate(cls, mac: str) -> None:
        mac = mac.strip()
        if not re.search(_MAC_REGEX, mac):
            raise ValueError(f"Unkown mac address format: {mac}", cls)

    def __repr__(self) -> str:
        return f"MacAddress({super().__repr__})"

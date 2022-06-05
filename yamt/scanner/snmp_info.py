from abc import ABC
from dataclasses import dataclass
from ..common.monad import Monad


@dataclass
class SNMPInfo:
    data: str

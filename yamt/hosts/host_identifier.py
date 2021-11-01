from abc import ABC
from pydantic import BaseModel


class IHostIdentifier(ABC):
    pass


class MacIdentifier(ABC):
    mac: str

from abc import ABC


class IHostIdentifier(ABC):
    pass


class IPIdentidifier(ABC):
    ip: str


class MacIdentifier(ABC):
    mac: str

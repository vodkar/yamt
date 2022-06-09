from yamt.common.model import YamtModelWithId

from .ip_interface import IPInterface
from .mac_address import MacAddress


class NetworkCard(YamtModelWithId):
    mac: MacAddress
    interfaces: list[IPInterface]

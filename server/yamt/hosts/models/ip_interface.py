from pydantic import IPvAnyAddress

from yamt.common.model import YamtModelWithId


class IPInterface(YamtModelWithId):
    ip: IPvAnyAddress

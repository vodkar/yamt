from common.model import YamtModel


class ISSHConnection(YamtModel):
    password: str
    port: int = 22

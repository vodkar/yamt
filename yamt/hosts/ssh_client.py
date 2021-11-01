from ipaddress import IPv4Address

from asyncssh import SSHClient as ASSHClient, connect


class SSHClient(ASSHClient):
    def __init__(
        self, ip: IPv4Address, port: int | None, username: str | None, password: str | None, client_keys
    ) -> None:
        self._ip = ip
        self._port = port
        super().__init__()

from functools import cache

from .connector import connect  # type: ignore
from .manager import SSHManager  # type: ignore
from .storage import SSHCredentialStorage  # type: ignore


@cache
def get_ssh_storage():
    return SSHCredentialStorage("ssh.yaml")

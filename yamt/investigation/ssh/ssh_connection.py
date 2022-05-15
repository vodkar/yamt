from yamt.common.model import YamtModel

from .ssh_credentials import SSHCredentials


class SSHConnection(YamtModel):
    creds: SSHCredentials

from pathlib import Path

from yamt.common.model import YamtModel


class SSHCredentials(YamtModel):
    key_path: Path

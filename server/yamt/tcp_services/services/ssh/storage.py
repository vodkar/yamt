from contextlib import contextmanager
from ipaddress import IPv4Address
from pathlib import Path
from typing import Any, Generator

import yaml

from yamt.hosts import Host
from yamt.tcp_services.services.ssh.models import SSHPasswordAuthentication


class SSHCredentialStorage:
    def __init__(self, yaml_path: str):
        self._yaml_path: str = yaml_path
        self._cached = False
        self._creds: dict[IPv4Address, SSHPasswordAuthentication] = self._open_yaml()

    def get_creds(self, host: Host) -> SSHPasswordAuthentication | None:
        return self._creds.get(host.ip)

    def add_ssh_host_creds(self, host: Host, creds: SSHPasswordAuthentication) -> None:
        self._creds[host.ip] = creds
        self._save()

    def _save(self):
        with open(self._yaml_path, "w") as f:
            yaml.dump({ip: cred.dict() for ip, cred in self._creds.items()}, f, yaml.Dumper)

    def _open_yaml(self) -> dict[IPv4Address, SSHPasswordAuthentication]:
        try:
            with open(self._yaml_path, "r") as f:
                return {ip: SSHPasswordAuthentication(**cred) for ip, cred in yaml.load(f, Loader=yaml.Loader).items()}
        except FileNotFoundError:
            Path(self._yaml_path).touch()
            with open(self._yaml_path, "r") as f:
                return {}
        except AttributeError:
            return {}

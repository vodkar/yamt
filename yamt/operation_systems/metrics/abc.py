from abc import ABC, abstractmethod

from yamt.tcp_services.services.ssh.manager import SSHManager

from .models import OSVersion


class OSVersionMetric(ABC):
    @abstractmethod
    async def get_os_version(self) -> OSVersion:
        pass


class SSHMetricManager(ABC):
    def __init__(self, ssh_manager: SSHManager) -> None:
        self._manager = ssh_manager
        super().__init__()

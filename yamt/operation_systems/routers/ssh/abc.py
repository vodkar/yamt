import re
from abc import ABC, abstractmethod, abstractproperty

from yamt.tcp_services.services.ssh import SSHManager


class SSHOutputChecker(ABC):
    @abstractmethod
    async def check_output(self, ssh: SSHManager) -> bool:
        pass


class RegexSSHOutputVerifier(SSHOutputChecker):
    async def check_output(self, ssh: SSHManager) -> bool:
        return bool(re.search(self.regex, await ssh.execute(self.cmd)))

    @abstractproperty
    def regex(self) -> str:
        return ""

    @abstractproperty
    def cmd(self) -> str:
        return ""

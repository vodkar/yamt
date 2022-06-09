import re

from yamt.tcp_services.services.ssh import SSHManager

from ..abc import OSVersionMetric, SSHMetricManager
from ..models import OSVersion

_OS_RELEASE_REGEX = r"""((VERSION=\"(?P<version>[\w\s]*)\")|(ID=(?P<id>[\w\s]*)\n)|(ID_LIKE=(?P<id_like>[\w\s]*)\n)|(NAME=\"(?P<name>[\w\s]*)\"))"""


class LinuxMetricManager(SSHMetricManager, OSVersionMetric):
    def __init__(self, ssh_manager: SSHManager) -> None:
        self._manager = ssh_manager

    async def get_os_version(self) -> OSVersion:
        os_rel_result = await self._manager.execute("egrep '^(VERSION|ID|ID_LIKE|NAME)=' /etc/os-release")
        uname_result = await self._manager.execute("uname -r")
        matches = re.match(_OS_RELEASE_REGEX, os_rel_result)
        assert matches, "Nothing found for this device"

        return OSVersion(
            core_version=uname_result,
            name=matches.group("name"),
            version=matches.group("version"),
            os_id=matches.group("id"),
            os_like_id=matches.group("id_like"),
        )

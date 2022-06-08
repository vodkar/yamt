from typing import Type

from yamt.tcp_services.services.ssh.manager import SSHManager

from ...metrics.abc import SSHMetricManager
from .abc import SSHOutputChecker


class SSHRouter:
    def __init__(self):
        self.checkers: list[SSHOutputChecker] = []
        self.metrics: list[Type[SSHMetricManager]] = []

    def register_metric(self, checker: SSHOutputChecker, metric: Type[SSHMetricManager]):
        self.checkers.append(checker)
        self.metrics.append(metric)

    async def get_metric(self, ssh: SSHManager) -> SSHMetricManager:
        for idx, checker in enumerate(self.checkers):
            if await checker.check_output(ssh):
                return self.metrics[idx](ssh)
        raise ValueError("No metrics for this device!")

from yamt.tcp_services.services.ssh.manager import SSHManager

from ...metrics.abc import SSHMetricManager
from .abc import SSHOutputChecker


class SSHRouter:
    def __init__(self):
        self.checkers: list[SSHOutputChecker] = []
        self.metrics: list[SSHMetricManager] = []

    def register_metric(self, checker: SSHOutputChecker, metric: SSHMetricManager):
        self.checkers.append(checker)
        self.metrics.append(metric)

    def get_metric(self, ssh: SSHManager) -> SSHMetricManager:
        for idx, checker in enumerate(self.checkers):
            if checker.check_output(ssh):
                return self.metrics[idx]
        raise ValueError("No metrics for this device!")

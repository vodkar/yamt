from yamt.cli_ui.host_actions.popup_action import OSVersionAction, PopupAction
from yamt.hosts import Host
from yamt.operation_systems.metrics.abc import OSVersionMetric, SSHMetricManager
from yamt.operation_systems.routers.ssh.router import SSHRouter
from yamt.tcp_services.scanner import TCPPortScanner
from yamt.tcp_services.services.ssh import SSHCredentialStorage, SSHManager
from yamt.tcp_services.services.ssh import connect as ssh_connect

from ..buttons import HostActionButton
from .name_action import InputSSHCredsAction, NameActionButton


async def get_host_options(
    host: Host, tcp_scanner: TCPPortScanner, ssh_creds_storage: SSHCredentialStorage, ssh_router: SSHRouter
) -> list[HostActionButton]:
    to_ret: list[HostActionButton] = []
    to_ret.append(NameActionButton(host))
    _, ports = await anext(tcp_scanner.scan_ports(host.ip, [22]))
    if 22 in ports:
        if creds := ssh_creds_storage.get_creds(host):
            async with ssh_connect(host, creds, 22) as ssh_manager:
                metrics = await ssh_router.get_metric(ssh_manager)
                to_ret.extend(options_from_metric(host, metrics))
        else:
            to_ret.append(InputSSHCredsAction(host, ssh_creds_storage))
    return to_ret


def options_from_metric(host: Host, metric_manager: SSHMetricManager):
    options: list[HostActionButton] = []
    if isinstance(metric_manager, OSVersionMetric):
        options.append(OSVersionAction(host, metric_manager))
    return options

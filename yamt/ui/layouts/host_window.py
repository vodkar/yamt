from prompt_toolkit.layout import HSplit, Window

from yamt.hosts.models.host import Host
from yamt.operation_systems.routers.ssh.router import SSHRouter
from yamt.tcp_services.scanner.tcp_port_scanner import TCPPortScanner
from yamt.tcp_services.services.ssh.storage import SSHCredentialStorage
from yamt.ui.layouts.host_info_window import HostInfoWindow

from .host_manager_window import HostManagerPane


class HostWindow(HSplit):
    def __init__(self, host_manager_window: HostManagerPane, host_info_window: HostInfoWindow):
        self._host_manager_window = host_manager_window
        self._host_info_window = host_info_window
        super().__init__([host_info_window, host_manager_window])
        # self.container = HSplit()

    async def render_host(
        self, host: Host, tcp_scanner: TCPPortScanner, ssh_creds_storage: SSHCredentialStorage, ssh_router: SSHRouter
    ):
        self._host_info_window.render_host_text(host)
        await self._host_manager_window.render_host_options(host, tcp_scanner, ssh_creds_storage, ssh_router)

    def select(self, to_return_container):
        self._host_manager_window.focus(to_return_container)

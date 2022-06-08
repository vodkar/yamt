from prompt_toolkit.application import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, ScrollablePane
from prompt_toolkit.widgets import Frame, TextArea

from yamt.hosts.models.host import Host
from yamt.operation_systems.routers.ssh.router import SSHRouter
from yamt.tcp_services.scanner.tcp_port_scanner import TCPPortScanner
from yamt.tcp_services.services.ssh.storage import SSHCredentialStorage
from yamt.ui.host_actions import get_host_options

from ..buttons import HostActionButton
from .utils import HasFocusMixin


class HostManagerPane(ScrollablePane, HasFocusMixin):
    def __init__(self):
        self._current_idx = 0
        super().__init__(HSplit([]))

    async def render_host_options(
        self, host: Host, tcp_scanner: TCPPortScanner, ssh_creds_storage: SSHCredentialStorage, ssh_router: SSHRouter
    ):
        self._buttons = await get_host_options(host, tcp_scanner, ssh_creds_storage, ssh_router)
        self.content = HSplit(self._buttons)
        self._host = host

    def focus(self, to_return_container):
        self._current_idx = 0
        self._to_return_container = to_return_container
        super().focus()

    def get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up", filter=self.has_focus)
        def _up(event):
            self._current_idx = (self._current_idx - 1) % len(self._buttons)
            get_app().layout.focus(self._buttons[self._current_idx].body)

        @kb.add("down", filter=self.has_focus)
        def _down(event):
            self._current_idx = (self._current_idx + 1) % len(self._buttons)
            get_app().layout.focus(self._buttons[self._current_idx].body)

        @kb.add("escape")
        def _return(event):
            get_app().layout.focus(self._to_return_container)

        return kb

    def get_host(self) -> Host:
        assert self._host
        return self._host

from prompt_toolkit.layout import HSplit, Window

from yamt.hosts.models.host import Host
from yamt.ui.layouts.host_info_window import HostInfoWindow

from .host_manager_window import HostManagerWindow


class HostWindow(Window):
    def __init__(self, host_manager_window: HostManagerWindow, host_info_window: HostInfoWindow):
        super().__init__()
        self._host_manager_window = host_manager_window
        self._host_info_window = host_info_window
        self.container = HSplit([host_manager_window, host_info_window])

    def render_host(self, host: Host):
        self._host_info_window.render_host_text(host)
        self._host_manager_window.render_host_options(host)

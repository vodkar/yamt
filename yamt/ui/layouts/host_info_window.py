from prompt_toolkit.layout import FormattedTextControl, Window

from yamt.hosts import Host


class HostInfoWindow(Window):
    def __init__(self):
        self._current_text: str = ""
        super().__init__()
        self.render()

    def render(self):
        self.content = FormattedTextControl(text=self._current_text)

    def render_host_text(self, host: Host):
        self._current_text = f"IP: {host.ip}\nMAC: {host.mac}\nName: {host.name}"
        self.render()

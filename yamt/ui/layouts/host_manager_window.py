from prompt_toolkit.layout import HSplit, ScrollablePane, Window
from prompt_toolkit.widgets import Frame, TextArea

from yamt.hosts.models.host import Host


class HostManagerWindow(Window):
    def __init__(self):
        super().__init__()
        self.container = ScrollablePane(HSplit([Frame(TextArea(text=f"label-{i}")) for i in range(20)]))

    def render_host_options(self, host: Host):
        pass

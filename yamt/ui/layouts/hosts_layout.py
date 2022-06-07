from aioreactive import AsyncObserver
from prompt_toolkit.formatted_text import HTML, merge_formatted_text
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Dimension, FormattedTextControl, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.margins import ScrollbarMargin

from yamt.hosts import Host

from .host_window import HostWindow


class HostsLayoutV2(AsyncObserver[Host]):
    def render_host(self, host: Host):
        return HTML(f'<style fg="red">{host.ip}</style>')

    def __init__(self, hosts: list[Host], host_window: HostWindow):
        self.host_window: HostWindow = host_window
        self.host_entries = hosts
        self.entries = [self.render_host(host) for host in hosts]
        self.selected_line = 1
        self.container = Window(
            content=FormattedTextControl(
                text=self._get_formatted_text,
                focusable=True,
                key_bindings=self._get_key_bindings(),
            ),
            style="class:select-box",
            height=Dimension(preferred=10, max=10),
            cursorline=True,
            right_margins=[
                ScrollbarMargin(display_arrows=True),
            ],
        )

    def _get_formatted_text(self):
        result = []
        for i, entry in enumerate(self.entries):
            if i == self.selected_line:
                result.append([("[SetCursorPosition]", "")])
            result.append(entry)
            result.append("\n")

        return merge_formatted_text(result)

    def _get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up")
        async def _go_up(event) -> None:
            self.selected_line = (self.selected_line - 1) % len(self.entries)
            self.host_window.render_host(self.host_entries[self.selected_line])

        @kb.add("down")
        async def _go_down(event) -> None:
            self.selected_line = (self.selected_line + 1) % len(self.entries)
            self.host_window.render_host(self.host_entries[self.selected_line])

        @kb.add("c-m")
        async def _go_enter(event) -> None:
            self.host_window.focus()

        return kb

    def __pt_container__(self):
        return self.container

    async def asend(self, value: Host):
        self.host_entries.append(value)
        self.entries.append(self.render_host(value))

    async def aclose(self) -> None:
        pass

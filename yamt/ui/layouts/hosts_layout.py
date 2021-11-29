from aioreactive import AsyncObserver
from aioreactive.types import AsyncObservable
from prompt_toolkit.formatted_text import HTML, merge_formatted_text
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import (
    AnyContainer,
    Dimension,
    FormattedTextControl,
    HSplit,
    Layout,
    VSplit,
    Window,
)
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.widgets import RadioList

from yamt.hosts import Host


class HostsLayout(RadioList, AsyncObserver):
    def __init__(self, hosts: list[Host]) -> None:
        super().__init__(list(map(self.render_host, hosts)))

    def render_host(self, host: Host):
        return (str(host.ip), HTML(f'<style bg="red" fg="white">{host.ip}</style>'))

    async def asend(self, host: Host):
        self.values.append(self.render_host(host))

    async def aclose(self) -> None:
        pass


class HostsLayoutV2(AsyncObserver):
    def render_host(self, host: Host):
        return HTML(f'<style fg="red">{host.ip}</style>')

    def __init__(self, hosts: list[Host], selected_subject: AsyncObservable[Host]):
        self.selected_subject = selected_subject
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
            height=Dimension(preferred=5, max=5),
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
            await self.selected_subject.asend(self.host_entries[self.selected_line])

        @kb.add("down")
        async def _go_up(event) -> None:
            self.selected_line = (self.selected_line + 1) % len(self.entries)
            await self.selected_subject.asend(self.host_entries[self.selected_line])

        return kb

    def __pt_container__(self):
        return self.container

    async def asend(self, host: Host):
        self.host_entries.append(host)
        self.entries.append(self.render_host(host))

    async def aclose(self) -> None:
        pass


class HostInfoWindow(Window, AsyncObserver):
    def __init__(self, *args, **kwargs):
        self._current_text = ""
        super().__init__(content=FormattedTextControl(text=self.get_current_text))

    @property
    def get_current_text(self):
        return self._current_text

    def render_host_text(self, host: Host):
        return f"IP: {host.ip}\nMAC: {host.mac}\nName: {host.name}"

    async def asend(self, host: Host):
        self._current_text = self.render_host_text(host)

    async def aclose(self) -> None:
        pass

    async def athrow(self, error: Exception) -> None:
        pass

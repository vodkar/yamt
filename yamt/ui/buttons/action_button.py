from typing import Any, Callable, Coroutine

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import Frame, TextArea

from yamt.hosts import Host


class HostActionButton(Frame):
    def __init__(self, host: Host, text_content: str, on_enter: Coroutine[Any, Any, Any] | None = None) -> None:
        if on_enter:
            self.on_enter = on_enter
        self.host = host
        super().__init__(TextArea(text=text_content), key_bindings=self._get_key_bindings())

    async def on_enter(self, event: Any, host: Host):
        pass

    def _get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("c-m")
        async def action(event: Any):
            await self.on_enter(event, self.host)

        return kb

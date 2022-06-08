from typing import Any, Coroutine

from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.styles import Style

from yamt.hosts import Host
from yamt.operation_systems.metrics.abc import OSVersionMetric, SSHMetricManager
from yamt.tcp_services.services.ssh.manager import SSHManager

from ..buttons import HostActionButton


class PopupAction(HostActionButton):
    def __init__(self, host: Host, button_text: str, title: str = "", text: str = "") -> None:
        self._title = title
        self._text = text
        super().__init__(host, button_text)

    async def on_enter(self, event: Any, host: Host):
        style = Style.from_dict(
            {
                "dialog": "bg:#000000",
                "dialog frame.label": "bg:#ffffff #000000",
                "dialog.body": "bg:#000000 #00ff00",
            }
        )
        await message_dialog(title=self._title, text=self._text, style=style).run_async()


class OSVersionAction(PopupAction):
    def __init__(self, host: Host, metric: OSVersionMetric) -> None:
        self.metric = metric
        super().__init__(host, "Get OS version")

    async def on_enter(self, event: Any, host: Host):
        style = Style.from_dict(
            {
                "dialog": "bg:#000000",
                "dialog frame.label": "bg:#ffffff #000000",
                "dialog.body": "bg:#000000 #00ff00",
            }
        )
        version = await self.metric.get_os_version()
        await message_dialog(title="OS Version", text=str(version), style=style).run_async()

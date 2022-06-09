from typing import Any, Coroutine

from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.styles import Style

from yamt.hosts import Host
from yamt.tcp_services.services.ssh import SSHCredentialStorage
from yamt.tcp_services.services.ssh.models import SSHPasswordAuthentication

from ..buttons import HostActionButton


class NameActionButton(HostActionButton):
    def __init__(self, host: Host) -> None:
        if host.name:
            super().__init__(
                host,
                "Update name",
            )
        else:
            super().__init__(host, "Set name")

    async def on_enter(self, event: Any, host: Host):
        style = Style.from_dict(
            {
                "dialog": "bg:#000000",
                "dialog frame.label": "bg:#ffffff #000000",
                "dialog.body": "bg:#000000 #00ff00",
            }
        )
        text = await input_dialog("Set new name: ", style=style).run_async()
        host.name = text


class InputSSHCredsAction(HostActionButton):
    def __init__(self, host: Host, ssh_creds_storage: SSHCredentialStorage) -> None:
        super().__init__(
            host,
            "Set ssh credentials",
        )
        self.ssh_creds_storage = ssh_creds_storage

    async def on_enter(self, event: Any, host: Host):
        style = Style.from_dict(
            {
                "dialog": "bg:#000000",
                "dialog frame.label": "bg:#ffffff #000000",
                "dialog.body": "bg:#000000 #00ff00",
            }
        )
        ssh_user = await input_dialog("Set ssh user: ", style=style).run_async()
        ssh_password = await input_dialog("Set user password: ", style=style, password=True).run_async()
        self.ssh_creds_storage.add_ssh_host_creds(
            host, SSHPasswordAuthentication(user=ssh_user, password=ssh_password)
        )

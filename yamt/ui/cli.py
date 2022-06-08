import asyncio
from ipaddress import IPv4Address, IPv4Network

from aioreactive import AsyncSubject, from_async_iterable
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import AnyContainer, HSplit, VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import (
    Box,
    Button,
    Checkbox,
    Dialog,
    Label,
    RadioList,
    TextArea,
)

from yamt.hosts.services import ARPScanner
from yamt.operation_systems.metrics.ssh import LinuxMetricManager
from yamt.operation_systems.routers.ssh import LinuxSSHOutputVerifier, SSHRouter
from yamt.tcp_services.scanner.stealth_port_scanner import TCPStealthPortScanner
from yamt.tcp_services.scanner.tcp_port_scanner import TCPPortScanner
from yamt.tcp_services.services.ssh.storage import SSHCredentialStorage
from yamt.ui.layouts import HostInfoWindow, HostManagerPane, HostsLayoutV2, HostWindow


async def redraw_loop(app):
    await asyncio.sleep(1)
    app.invalidate()


def indented(container: AnyContainer, amount: int = 2) -> AnyContainer:
    return VSplit([Label("", width=amount), container])


async def run():
    host_window = HostWindow(HostManagerPane(), HostInfoWindow())
    tcp_scanner: TCPPortScanner = TCPStealthPortScanner()
    ssh_router = SSHRouter()
    ssh_router.register_metric(LinuxSSHOutputVerifier(), LinuxMetricManager)
    hosts_layout = HostsLayoutV2(
        [],
        host_window,
        tcp_scanner,
        SSHCredentialStorage("ssh.yaml"),
        ssh_router,
    )
    root_container = VSplit(
        [
            hosts_layout,
            Window(width=1, char="|"),
            host_window,
        ]
    )

    layout = Layout(root_container)

    app = Application(layout=layout, full_screen=True)

    service = ARPScanner()
    gen = service.scan_network(IPv4Network("192.168.0.0/24"))
    asyncio.create_task(from_async_iterable(gen.__aiter__()).subscribe_async(hosts_layout))

    await asyncio.gather(app.run_async(), redraw_loop(app))


if __name__ == "__main__":
    asyncio.new_event_loop().run_until_complete(run())

import asyncio
from ipaddress import IPv4Address, IPv4Network

from aioreactive import AsyncSubject, from_async_iterable
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import AnyContainer, VSplit, Window
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

from yamt.hosts import Host, MacAddress
from yamt.network.discovery import DiscoveryService
from yamt.network.scan import ARPScanner
from yamt.ui.layouts.hosts_layout import HostInfoWindow, HostsLayout, HostsLayoutV2


async def redraw_loop(app):
    await asyncio.sleep(1)
    app.invalidate()


def indented(container: AnyContainer, amount: int = 2) -> AnyContainer:
    return VSplit([Label("", width=amount), container])


async def run():

    selected_subject = AsyncSubject()
    hosts_layout = HostsLayoutV2([], selected_subject)
    host_info_window = HostInfoWindow()
    await selected_subject.subscribe_async(host_info_window)
    root_container = VSplit(
        [
            indented(hosts_layout),
            Window(width=1, char="|"),
            host_info_window,
        ]
    )

    layout = Layout(root_container)

    app = Application(layout=layout)

    service = DiscoveryService(ARPScanner())
    gen = service.scanner.scan_network(IPv4Network("192.168.2.0/24"))
    asyncio.create_task(from_async_iterable(gen.__aiter__()).subscribe_async(hosts_layout))

    await asyncio.gather(app.run_async(), redraw_loop(app))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())

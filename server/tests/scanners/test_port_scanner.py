from ipaddress import IPv4Address

from pytest import mark

from yamt.tcp_services.scanner.port_scanner import TCPStealthUdpPortScanner


@mark.asyncio
async def test_tcp_port_scanner():
    scanner = TCPStealthUdpPortScanner()
    async for val in scanner.scan_ports([IPv4Address("192.168.221.128")], [22, 1337, 8080]):
        print(val)

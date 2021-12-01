from pytest import fixture, mark

from yamt.network.scan.arp_scan import ARPScanner


@fixture
def arp_scanner():
    return ARPScanner()


@mark.asyncio
async def test_network_arp_scan(arp_scanner: ARPScanner, test_network):
    async for host in arp_scanner.scan_network(test_network):
        print(host)

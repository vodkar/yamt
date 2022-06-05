from ipaddress import IPv4Network

from pytest import fixture

from .hosts.fixtures import *


@fixture
async def test_network():
    return IPv4Network("192.168.1.0/24")

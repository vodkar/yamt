from importlib import import_module
from ipaddress import IPv4Network

from pytest import fixture

import_module("tests.fixtures")


@fixture
async def test_network():
    return IPv4Network("192.168.1.0/24")

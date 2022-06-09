from ipaddress import IPv4Address

import yaml
from faker import Faker

from yamt.hosts import Host, HostStorage, MacAddress
from yamt.hosts.host_storage import HostStorage


def test_host_storage(host_storage: HostStorage, host_storage_path: str, faker: Faker):
    host1 = Host(ip=IPv4Address(faker.ipv4()), mac=MacAddress(faker.mac_address()), name=faker.name())
    host2 = Host(ip=IPv4Address(faker.ipv4()), mac=MacAddress(faker.mac_address()), name=faker.name())
    host_storage.add_hosts([host1, host2])
    assert list(host_storage.get_hosts()) == [host1, host2]

    with open(host_storage_path, "r") as f:
        d = yaml.load(f, yaml.Loader)
        assert d[0] == host1.dict()
        assert d[1] == host2.dict()

    host_storage_second = HostStorage(host_storage_path)
    host_storage.add_hosts([host1, host2])
    assert list(host_storage_second.get_hosts()) == [host1, host2]
    host3 = Host(ip=IPv4Address(faker.ipv4()), mac=MacAddress(faker.mac_address()), name=faker.name())
    host_storage_second.add_hosts([host3])
    assert list(host_storage_second.get_hosts()) == [host1, host2, host3]

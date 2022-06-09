from ipaddress import IPv4Address
from typing import Any

import pytest
import yaml
from faker import Faker

from yamt.hosts import Host, HostGroup, HostGroupStorage, HostStorage, MacAddress


@pytest.fixture
def host_group_storage_path(temp_dir: str):
    return f"{temp_dir}/host_group_storage.yaml"


@pytest.fixture
def host_group_storage(host_group_storage_path: str, host_storage: HostStorage):
    return HostGroupStorage(host_group_storage_path, host_storage)


def test_host_group_storage(host_storage: HostStorage, host_group_storage: HostGroupStorage, host_group_storage_path: str, faker: Faker):
    host1 = Host(ip=IPv4Address(faker.ipv4()), mac=MacAddress(faker.mac_address()), name=faker.name())
    host2 = Host(ip=IPv4Address(faker.ipv4()), mac=MacAddress(faker.mac_address()), name=faker.name())
    host_storage.add_hosts([host1, host2])
    group = HostGroup(name=faker.name(), hosts=[host1, host2])
    host_group_storage.add_host_groups([group])
    assert [group] == list(host_group_storage.get_host_groups())
    
    with open(host_group_storage_path) as f:
        d: list[dict[str, Any]] = yaml.load(f, yaml.Loader)
        assert d[0]["name"] == group.name and d[0]['hosts'] == [{"ip": host.ip} for host in group.hosts]

    host_group_storage_second = HostGroupStorage(host_group_storage_path, host_storage)
    assert [group] == list(host_group_storage_second.get_host_groups())
    host3 = Host(ip=IPv4Address(faker.ipv4()), mac=MacAddress(faker.mac_address()), name=faker.name())
    group_second = HostGroup(name=faker.name(), hosts=[host3])
    host_group_storage_second.add_host_groups([group_second])
    assert [group, group_second] == list(host_group_storage_second.get_host_groups())

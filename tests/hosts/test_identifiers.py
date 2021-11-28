import pytest
from pydantic import ValidationError

from yamt.hosts.host_identifier import MacAddress


def test_mac_identifier():
    mac = MacAddress("ff:ff:ff:ff:ff:ff")
    assert mac
    mac = MacAddress("ff:ff:ff:ff:ff:ff ")
    assert mac

    with pytest.raises(ValidationError):
        mac = MacAddress("ff:ff:ff:ff:ff:ff 123")

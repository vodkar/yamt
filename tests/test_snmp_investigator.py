from ipaddress import IPv4Address

import pytest

from yamt.scanner.snmp_investigator import SNMPInvestigator


@pytest.mark.asyncio
async def test_investigator_centos():
    invetigator = SNMPInvestigator()
    async for ainfo in invetigator.get_info(IPv4Address("192.168.0.103")):
        print(ainfo.data)

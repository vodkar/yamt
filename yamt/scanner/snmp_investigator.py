from ipaddress import IPv4Address
from typing import AsyncGenerator, Generator, Tuple

from pysnmp.hlapi import (
    UdpTransportTarget,
    SnmpEngine,
    CommunityData,
    ContextData,
    ObjectType,
    ObjectIdentity,
    getCmd,
)

from .snmp_info import SNMPInfo


class SNMPInvestigator:
    async def get_info(self, ip: IPv4Address) -> AsyncGenerator[SNMPInfo, None]:
        iter: Generator[tuple, None, None] = getCmd(
            SnmpEngine(),
            CommunityData("kek228", mpModel=0),
            UdpTransportTarget((str(ip), 161)),
            ContextData(),
            ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)),
        )
        for vals in iter:
            yield await self._to_info(*vals)

    async def _to_info(self, errorIndication, errorStatus, errorIndex, varBinds) -> SNMPInfo:
        if errorIndication:
            return SNMPInfo(errorIndication)

        elif errorStatus:
            return SNMPInfo(
                "%s at %s"
                % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or "?")
            )

        else:
            return SNMPInfo(
                "\n".join([" = ".join([x.prettyPrint() for x in varBind]) for varBind in varBinds])
            )

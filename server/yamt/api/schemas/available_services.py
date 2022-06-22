from __future__ import annotations

from enum import IntFlag


class AvailableServices(IntFlag):
    INIT = 0
    SSH = 1

    @classmethod
    def from_ports(cls, ports: list[int]) -> AvailableServices:
        init = AvailableServices.INIT
        if 22 in ports:
            init = init | cls.SSH
        return init

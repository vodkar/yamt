from contextlib import asynccontextmanager
from typing import AsyncGenerator

import asyncssh

from yamt.hosts import Host

from .manager import SSHManager
from .models import SSHPasswordAuthentication


@asynccontextmanager
async def connect(
    host: Host, auth: SSHPasswordAuthentication, port: int = 22
) -> AsyncGenerator[SSHManager, None]:
    async with SSHManager(
        await asyncssh.connect(str(host.ip), port, username=auth.user, password=auth.password)
    ) as manager:
        yield manager

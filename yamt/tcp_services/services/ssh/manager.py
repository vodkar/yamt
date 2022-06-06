from types import TracebackType
from typing import Optional, Type

from asyncssh.connection import SSHClientConnection


class SSHManager:
    def __init__(self, connection: SSHClientConnection):
        self.conn = connection
        
    async def execute(self, cmd: str) -> str:
        result = await self.conn.run(cmd)
        return str(result)

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, _exc_type: Optional[Type[BaseException]],
                        _exc_value: Optional[BaseException],
                        _traceback: Optional[TracebackType]):
        return await self.conn.__aexit__(_exc_type, _exc_value, _traceback)
        
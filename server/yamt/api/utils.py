import asyncio
from typing import Any, Callable, Coroutine


async def run_task(task: Callable[[Any], Coroutine[Any, Any, Any]], *args: Any, **kwargs: Any):
    asyncio.create_task(task(*args, **kwargs))

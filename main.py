#!/usr/bin/python
import asyncio

from yamt.ui import run

if __name__ == "__main__":
    asyncio.new_event_loop().run_until_complete(run())

import aiohttp

from .mac_address import MacAddress


async def get_manufacturer_by_mac(mac: MacAddress) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.macvendors.com/{mac}") as response:
            return await response.text()

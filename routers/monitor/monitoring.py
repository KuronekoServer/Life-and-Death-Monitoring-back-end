from httpx import AsyncClient

import asyncio
from db.monitor import Monitor


async def start(pool):
    while True:
        print("Checking monitors...")
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                monitor = Monitor(cursor)
                for m in await monitor.get_all():
                    response = await AsyncClient().get(monitor["url"])
                    await monitor.http_log(m[4], response.status_code)
        await asyncio.sleep(60)
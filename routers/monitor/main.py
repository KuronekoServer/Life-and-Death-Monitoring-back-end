from core import Router
from db.monitor import Monitor
from .monitoring import start

import asyncio


router = Router(prefix="/api/monitor")


@router.on_event("startup")
async def startup():
    async with router.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await Monitor(cursor).prepare_table()
    asyncio.create_task(start(router.pool))
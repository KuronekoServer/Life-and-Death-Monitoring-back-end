from fastapi import Cookie

from core import Router
from db.account import Account


router = Router(prefix="/api/status")


@router.post("/create")
async def create(token: Cookie(None)):
    "Creates a status."
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    async with router.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            account = Account(cursor)
            user = await account.get_account(token)
            if user is None:
                raise HTTPException(status_code=401, detail="Unauthorized")
            await account.create_status(user[0], body)
            return {"status": "ok"}
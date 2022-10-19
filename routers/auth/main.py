from httpx import AsyncClient
from .db import Account

from fastapi import Query, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.requests import Request

from data import CONFIG
from core import Router

import random
import string


router = Router(prefix="/api/auth")
client = AsyncClient()

def make_token():
    "Generate a random token."
    return "".join(random.choices(string.ascii_letters + string.digits, k=32))


@router.on_event("startup")
async def startup():
    "Prepare the accounts table."
    await Account(router.pool).prepare_table()


@router.get("/login")
async def login():
    "Redirects to the login page."
    return RedirectResponse(
        "https://github.com/login/oauth/authorize"
        f"?client_id={CONFIG['github']['client_id']}"
        f"&redirect_uri={CONFIG['github']['redirect_uri']}"
        "&scope=user"
    )

@router.get("/callback")
async def callback(req: Request, code: str | None = Query(default=None)):
    "Callback for the login page."
    if code is None:
        raise HTTPException(status_code=400, detail="Missing code")
    response = await client.post("https://github.com/login/oauth/access_token", headers={
        "Accept": "application/json"
    }, data={
        "client_id": CONFIG["github"]["client_id"],
        "client_secret": CONFIG["github"]["client_secret"],
        "code": code,
        "redirect_uri": CONFIG["github"]["redirect_uri"]
    })
    response.raise_for_status()
    response = await client.get("https://api.github.com/user", headers={
        "Authorization": f"Bearer {response.json()['access_token']}"
    })
    response.raise_for_status()
    account = Account(req.app.state.pool)
    await account.create_account(response.json()["id"], response.json()["login"], make_token())
    res = RedirectResponse(CONFIG["frontend"]["url"])
    res.set_cookie("token", make_token())
    return res
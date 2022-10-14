from httpx import AsyncClient
from sanic import Blueprint, Sanic, response


bp = Blueprint("auth", url_prefix="/api/auth")
client = AsyncClient()


@bp.get("/login")
async def login(_):
    return response.redirect("https://google.com")
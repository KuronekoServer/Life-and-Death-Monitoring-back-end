from core import MonitoringApp
from data import CONFIG

from os import listdir
from importlib import import_module

from uvicorn import run
from aiomysql import create_pool


app = MonitoringApp()


@app.get("/")
async def index():
    return "Hello World!"


@app.on_event("startup")
async def startup():
    app.state.pool = await create_pool(**CONFIG["mysql"])
    for filename in listdir("routers"):
        if not filename.startswith("_"):
            router = import_module(f"routers.{filename}").router
            router.pool = app.state.pool
            app.include_router(router)


@app.on_event("shutdown")
async def shutdown():
    app.state.pool.close()
    await app.state.pool.wait_closed()


if __name__ == "__main__":
    run(
        "app:app", host=CONFIG["fastapi"]["host"],
        port=CONFIG["fastapi"]["port"], reload=CONFIG["debug"]
    )
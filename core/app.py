from sanic import Sanic

from aiomysql import Pool, create_pool

from data import CONFIG


class MonitoringApp(Sanic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_listener(self.connect_to_db, "before_server_start")
    
    async def connect_to_db(self, app, _):
        app.ctx.pool: Pool = await create_pool(**CONFIG["mysql"])
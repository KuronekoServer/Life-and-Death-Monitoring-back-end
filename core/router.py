from fastapi import APIRouter

from aiomysql import Pool


class Router(APIRouter):
    pool = Pool | None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
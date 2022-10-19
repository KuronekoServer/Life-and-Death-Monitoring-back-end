from toml import load

from typing import TypedDict


class Config(TypedDict):
    fastapi: dict
    db_url: str
    debug: bool
    github: dict
    frontend: dict


with open("config.toml", "r") as f:
    CONFIG: Config = load(f)
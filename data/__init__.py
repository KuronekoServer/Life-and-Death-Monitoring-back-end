from toml import load

from typing import TypedDict


class Config(TypedDict):
    sanic: dict
    mysql: dict


with open("config.toml", "r") as f:
    CONFIG: Config = load(f)
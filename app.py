from core import MonitoringApp
from data import CONFIG

from os import listdir
from importlib import import_module


app = MonitoringApp("monitor")


for filename in listdir("blueprints"):
    if not filename.startswith("_"):
        bp = import_module(f"blueprints.{filename}").bp
        bp.ctx = app.ctx
        app.blueprint(bp)


if __name__ == "__main__":
    app.run(**CONFIG["sanic"])
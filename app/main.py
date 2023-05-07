import importlib

from importlib import resources
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.shared.deps import get_settings


SETTINGS = get_settings()

app = FastAPI(root_path=SETTINGS.root_path, title="Messages API")

# include all routers
plugins = [f[:-3] for f in resources.contents("app.routers")
           if f.endswith(".py") and f[0] != "_"]
for plugin in plugins:
    router = importlib.import_module(f"app.routers.{plugin}")
    app.include_router(router.router)


# setup middleware
if SETTINGS.debug:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

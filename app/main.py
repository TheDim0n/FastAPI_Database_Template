import time

import importlib

from importlib import resources
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

from app.shared.deps import get_settings


SETTINGS = get_settings()

app = FastAPI(
    title="Messages API",
    root_path=SETTINGS.root_path,
    docs_url=None,
    redoc_url=None
)
app.mount("/static", StaticFiles(directory="static"), name="static")

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


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time * 1000} ms"
    return response


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=f"{SETTINGS.root_path}{app.openapi_url}",
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"{SETTINGS.root_path}/static/swagger-ui-bundle.js",
        swagger_css_url=f"{SETTINGS.root_path}/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

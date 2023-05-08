import asyncio
from typing import Generator

import pytest
import pytest_asyncio

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine

from app.shared.db.database import DataBase
from app.shared.deps import get_settings
from app.main import app


SQLALCHEMY_DATABASE_URL = get_settings().db_url

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

test_message = {"message": "test message"}


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:  # noqa: indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        app=app,
        base_url="http://localhost"
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_create_db():
    async with engine.begin() as conn:
        await conn.run_sync(DataBase.metadata.drop_all)
        await conn.run_sync(DataBase.metadata.create_all)


@pytest.mark.asyncio
async def test_create_message(client: AsyncClient):
    response = await client.post("/messages", json=test_message)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_read_created_message(client: AsyncClient):
    response = await client.get("/messages")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[-1]["message"] == test_message["message"]


@pytest.mark.asyncio
async def test_delete_message(client: AsyncClient):
    response = await client.get("/messages")
    assert response.status_code == 200

    id = response.json()[0]["id"]
    response = await client.delete(f"/messages/{id}")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_read_messages_after_delete(client: AsyncClient):
    response = await client.get("/messages")
    assert response.status_code == 200
    assert len(response.json()) == 0

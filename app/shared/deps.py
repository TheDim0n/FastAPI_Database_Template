from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.db.database import SessionLocal
from app.shared.config import Settings


@lru_cache()
def get_settings():
    return Settings()


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

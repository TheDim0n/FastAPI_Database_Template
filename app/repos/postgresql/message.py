from typing import List, Union

import sqlalchemy as sa

from fastapi import Depends, HTTPException
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.db.models import Message
from app.shared.deps import get_session
from app.shared.dto.message import MessageCreate


class MessageRepo:
    def __init__(
            self,
            session: Union[AsyncSession, Connection] = Depends(get_session)
    ) -> None:
        self.session: Union[AsyncSession, Connection] = session

    async def list(self) -> List[Message]:
        query = sa.select(Message)
        result = await self.session.execute(query)
        data = result.scalars().all()
        return data

    async def insert_item(self, item: MessageCreate) -> MessageCreate:
        result = await self.session.execute(
            sa.insert(Message).values(**item.dict()).returning(Message)
        )
        await self.session.commit()
        return result.scalar()

    async def remove_item(self, id: int) -> None:
        query = sa.select(Message).where(Message.id == id)
        result = await self.session.execute(query)
        if not result.scalar():
            raise HTTPException(
                status_code=404,
                detail=f"Message with id={id} not found"
            )
        await self.session.execute(
            sa.delete(Message).where(Message.id == id)
        )
        await self.session.commit()

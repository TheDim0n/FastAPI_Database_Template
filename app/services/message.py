from typing import List

from fastapi import Depends

from app.repos.postgresql.message import MessageRepo
from app.shared.dto.message import MessageDTO, MessageCreate


class MessageService:
    def __init__(self, repo: MessageRepo = Depends()) -> None:
        self.repo: MessageRepo = repo

    async def list(self) -> List[MessageDTO]:
        return await self.repo.list()

    async def add_item(self, item: MessageCreate) -> MessageDTO:
        return await self.repo.insert_item(item=item)

    async def remove_item(self, id: int) -> None:
        return await self.repo.remove_item(id=id)

from typing import List

from fastapi import APIRouter, Depends

from app.services.message import MessageService
from app.shared.dto.message import MessageDTO, MessageCreate

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.get('', summary="Read list of messages")
async def read_messages(
    service: MessageService = Depends()
) -> List[MessageDTO]:
    return await service.list()


@router.post('', summary="Add new message item", status_code=201)
async def insert_item(
    item: MessageCreate,
    service: MessageService = Depends()
) -> MessageDTO:
    return await service.add_item(item)


@router.delete('/{id}', summary="Remove message item by id", status_code=204)
async def remove_item(
    id: int,
    service: MessageService = Depends()
) -> None:
    return await service.remove_item(id)

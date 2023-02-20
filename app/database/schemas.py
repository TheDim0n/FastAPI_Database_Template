from pydantic import BaseModel
from uuid import UUID


class MessageBase(BaseModel):
    message: str


class MessageCreate(MessageBase):
    pass


class MessageDB(MessageBase):
    uuid: UUID or str

    class Config:
        orm_mode = True

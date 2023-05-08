from pydantic import BaseModel


class MessageCreate(BaseModel):
    message: str


class MessageDTO(MessageCreate):
    id: int

    class Config:
        orm_mode = True

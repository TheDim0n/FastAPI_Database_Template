import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from .database import DataBase


class Message(DataBase):
    __tablename__ = "message"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message = Column(String(), nullable=False)

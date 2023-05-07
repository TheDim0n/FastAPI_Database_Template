from sqlalchemy import Column, Integer, String

from .database import DataBase

from app.shared.deps import get_settings


SCHEMA = get_settings().db_schema


class Message(DataBase):
    __tablename__ = "message"
    __table_args__ = {
        "schema": SCHEMA
    }

    id = Column(Integer, primary_key=True)
    message = Column(String(), nullable=False)

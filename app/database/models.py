from sqlalchemy import Column, Integer, String

from .database import DataBase


class Message(DataBase):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    message = Column(String(), nullable=False)

from sqlalchemy import Column, Integer, String

from .database import DataBase

from app.shared.deps import get_settings


SCHEME = get_settings().db_scheme


class Message(DataBase):
    __tablename__ = "message"
    __table_args__ = {
        "scheme": SCHEME
    }

    id = Column(Integer, primary_key=True)
    message = Column(String(), nullable=False)

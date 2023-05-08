import sqlalchemy as sa

from .database import DataBase

from app.shared.deps import get_settings


SCHEMA = get_settings().db_schema


class Message(DataBase):
    __tablename__ = "message"
    __table_args__ = {
        "schema": SCHEMA
    }

    id = sa.Column(sa.Integer, primary_key=True)
    message = sa.Column(sa.String, nullable=False)

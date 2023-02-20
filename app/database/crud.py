from sqlalchemy.orm import Session
from uuid import UUID

from . import models, schemas


def create_message(db: Session, new_message: schemas.MessageCreate):
    db_message = models.Message(**new_message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return


def get_messages(db: Session):
    return db.query(models.Message).all()


def delete_message_by_uuid(db: Session, uuid: UUID):
    _ = db.query(models.Message).filter(models.Message.uuid == uuid).delete()
    db.commit()
    return

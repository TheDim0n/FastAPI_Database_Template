"""add init data

Revision ID: 34285860c86d
Revises: 359333400e7a
Create Date: 2023-05-07 23:12:12.253648

"""
from alembic import op
import sqlalchemy as sa

from app.repos.mock.message import MockMessageRepo
from app.shared.db.models import Message


# revision identifiers, used by Alembic.
revision = '34285860c86d'
down_revision = '359333400e7a'
branch_labels = None
depends_on = None


def upgrade():
    mock_message_repo = MockMessageRepo("./app/shared/mock/message.json")
    items = mock_message_repo.read()
    op.bulk_insert(
        Message.__table__,
        [item.dict() for item in items]
    )


def downgrade():
    op.execute(sa.delete(Message))

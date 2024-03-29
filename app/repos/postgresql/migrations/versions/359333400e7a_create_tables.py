"""create tables

Revision ID: 359333400e7a
Revises:
Create Date: 2023-05-07 22:57:53.038525

"""
from alembic import op
import sqlalchemy as sa

from app.shared.deps import get_settings

# revision identifiers, used by Alembic.
revision = '359333400e7a'
down_revision = None
branch_labels = None
depends_on = None


SCHEMA = get_settings().db_schema


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'message',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema=f'{SCHEMA}'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message', schema=f'{SCHEMA}')
    # ### end Alembic commands ###

"""Update identifier of Tweet

Revision ID: bbaea238cc0e
Revises: 0cca9c6154b8
Create Date: 2020-11-19 11:52:44.047981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbaea238cc0e'
down_revision = '0cca9c6154b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tweet', 'identifier',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tweet', 'identifier',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###
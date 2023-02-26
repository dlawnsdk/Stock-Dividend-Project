"""empty message

Revision ID: 5cf4ad4ad7cf
Revises: 4299b616ac71
Create Date: 2023-02-26 22:19:04.853512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cf4ad4ad7cf'
down_revision = '4299b616ac71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('board', sa.Column('modify_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('board', 'modify_date')
    # ### end Alembic commands ###

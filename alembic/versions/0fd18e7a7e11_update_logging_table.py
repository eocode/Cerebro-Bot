"""update logging table

Revision ID: 0fd18e7a7e11
Revises: b0b6b5083bbd
Create Date: 2022-09-27 20:06:11.205888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd18e7a7e11'
down_revision = 'b0b6b5083bbd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logging', sa.Column('message', sa.String(length=600), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logging', 'message')
    # ### end Alembic commands ###

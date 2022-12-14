"""update room table

Revision ID: fa7452845d35
Revises: 258726d6a0e9
Create Date: 2022-09-25 14:06:21.404349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa7452845d35'
down_revision = '258726d6a0e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('room', sa.Column('bathroom', sa.BIGINT(), nullable=False))
    op.add_column('room', sa.Column('kitchen', sa.BIGINT(), nullable=False))
    op.add_column('room', sa.Column('patio', sa.BIGINT(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('room', 'patio')
    op.drop_column('room', 'kitchen')
    op.drop_column('room', 'bathroom')
    # ### end Alembic commands ###

"""update logging table

Revision ID: 258726d6a0e9
Revises: fe32496aebde
Create Date: 2022-09-25 13:45:18.308883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '258726d6a0e9'
down_revision = 'fe32496aebde'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('action', table_name='logging')
    op.drop_index('module', table_name='logging')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('module', 'logging', ['module'], unique=False)
    op.create_index('action', 'logging', ['action'], unique=False)
    # ### end Alembic commands ###
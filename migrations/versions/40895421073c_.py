"""empty message

Revision ID: 40895421073c
Revises: 92f7ab77a8d9
Create Date: 2023-03-20 14:41:47.024213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40895421073c'
down_revision = '92f7ab77a8d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###

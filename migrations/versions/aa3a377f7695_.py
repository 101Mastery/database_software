"""empty message

Revision ID: aa3a377f7695
Revises: debafc0c5bea
Create Date: 2017-06-24 20:02:21.140580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa3a377f7695'
down_revision = 'debafc0c5bea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('key', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'key')
    # ### end Alembic commands ###

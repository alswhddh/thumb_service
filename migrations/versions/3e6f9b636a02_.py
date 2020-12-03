"""empty message

Revision ID: 3e6f9b636a02
Revises: 436e7a993e07
Create Date: 2020-11-06 16:41:06.456374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e6f9b636a02'
down_revision = '436e7a993e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thumbnail', sa.Column('category', sa.String(length=100), nullable=False))
    op.drop_column('thumbnail', 'categori')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thumbnail', sa.Column('categori', sa.VARCHAR(length=100), nullable=False))
    op.drop_column('thumbnail', 'category')
    # ### end Alembic commands ###

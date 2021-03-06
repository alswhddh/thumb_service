"""empty message

Revision ID: e4b8e9bb3c7e
Revises: 4ecc22933767
Create Date: 2020-11-05 09:29:07.183779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4b8e9bb3c7e'
down_revision = '4ecc22933767'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thumbnail', sa.Column('categori', sa.String(length=100), nullable=False))
    op.alter_column('thumbnail', 'imgAdr',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('thumbnail', 'imgAdr',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.drop_column('thumbnail', 'categori')
    # ### end Alembic commands ###

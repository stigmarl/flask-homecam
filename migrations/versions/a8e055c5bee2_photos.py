"""photos

Revision ID: a8e055c5bee2
Revises: a76e40f6375c
Create Date: 2019-02-06 14:25:24.006341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8e055c5bee2'
down_revision = 'a76e40f6375c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=64), nullable=True),
    sa.Column('file_path', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_path')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo')
    # ### end Alembic commands ###

"""empty message

Revision ID: 26db5c92c118
Revises: 
Create Date: 2021-04-07 03:22:20.095901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26db5c92c118'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('first_surname', sa.String(length=100), nullable=False),
    sa.Column('second_surname', sa.String(length=100), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('user_image', sa.String(length=2000), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

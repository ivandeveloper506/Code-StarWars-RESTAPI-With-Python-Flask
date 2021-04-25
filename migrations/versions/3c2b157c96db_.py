"""empty message

Revision ID: 3c2b157c96db
Revises: 
Create Date: 2021-04-24 22:46:35.272467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c2b157c96db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('climate_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('eye_color_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gender_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('hair_color_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('skin_color_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('terrain_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('first_surname', sa.String(length=100), nullable=False),
    sa.Column('second_surname', sa.String(length=100), nullable=True),
    sa.Column('user_image', sa.String(length=2000), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicle_class_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=False),
    sa.Column('favorite_type', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.Date(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('people_image', sa.String(length=2000), nullable=True),
    sa.Column('gender_cat_id', sa.Integer(), nullable=True),
    sa.Column('hair_color_cat_id', sa.Integer(), nullable=True),
    sa.Column('skin_color_cat_id', sa.Integer(), nullable=True),
    sa.Column('eye_color_cat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['eye_color_cat_id'], ['eye_color_cat.id'], ),
    sa.ForeignKeyConstraint(['gender_cat_id'], ['gender_cat.id'], ),
    sa.ForeignKeyConstraint(['hair_color_cat_id'], ['hair_color_cat.id'], ),
    sa.ForeignKeyConstraint(['skin_color_cat_id'], ['skin_color_cat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=50), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('planet_image', sa.String(length=2000), nullable=True),
    sa.Column('climate_cat_id', sa.Integer(), nullable=True),
    sa.Column('terrain_cat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['climate_cat_id'], ['climate_cat.id'], ),
    sa.ForeignKeyConstraint(['terrain_cat_id'], ['terrain_cat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('manufacturer', sa.String(length=100), nullable=True),
    sa.Column('cost_in_credits', sa.Integer(), nullable=True),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('consumables', sa.String(length=100), nullable=True),
    sa.Column('vehicle_image', sa.String(length=2000), nullable=True),
    sa.Column('vehicle_class_cat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['vehicle_class_cat_id'], ['vehicle_class_cat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('people')
    op.drop_table('favorite')
    op.drop_table('vehicle_class_cat')
    op.drop_table('user')
    op.drop_table('terrain_cat')
    op.drop_table('skin_color_cat')
    op.drop_table('hair_color_cat')
    op.drop_table('gender_cat')
    op.drop_table('eye_color_cat')
    op.drop_table('climate_cat')
    # ### end Alembic commands ###
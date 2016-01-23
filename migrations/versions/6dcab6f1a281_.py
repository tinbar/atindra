"""empty message

Revision ID: 6dcab6f1a281
Revises: None
Create Date: 2016-01-22 17:48:41.855334

"""

# revision identifiers, used by Alembic.
revision = '6dcab6f1a281'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('mobile_device_id', sa.String(), nullable=True),
    sa.Column('salt', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('city_of_residence', sa.String(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('user_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.Column('resource_uri', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_token')
    op.drop_table('user')
    ### end Alembic commands ###
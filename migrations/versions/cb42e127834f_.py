"""empty message

Revision ID: cb42e127834f
Revises: 
Create Date: 2020-04-14 02:01:14.040886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb42e127834f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=40), nullable=False),
    sa.Column('lname', sa.String(length=40), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('location', sa.String(length=40), nullable=True),
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###

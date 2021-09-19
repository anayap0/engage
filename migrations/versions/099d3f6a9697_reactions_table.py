"""Reactions table

Revision ID: 099d3f6a9697
Revises: 21130c2ebede
Create Date: 2020-12-19 11:21:04.453646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '099d3f6a9697'
down_revision = '21130c2ebede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reactions')
    # ### end Alembic commands ###
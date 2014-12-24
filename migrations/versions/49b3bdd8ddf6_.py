"""empty message

Revision ID: 49b3bdd8ddf6
Revises: 59c106871e7b
Create Date: 2014-12-19 18:08:33.294321

"""

# revision identifiers, used by Alembic.
revision = '49b3bdd8ddf6'
down_revision = '59c106871e7b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('persons')
    ### end Alembic commands ###
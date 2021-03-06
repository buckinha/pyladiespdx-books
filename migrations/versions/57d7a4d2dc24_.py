"""empty message

Revision ID: 57d7a4d2dc24
Revises: None
Create Date: 2015-04-13 21:34:30.588862

"""

# revision identifiers, used by Alembic.
revision = '57d7a4d2dc24'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    ### end Alembic commands ###

"""Added weight and height columns

Revision ID: 345fbdd1d04d
Revises: 
Create Date: 2023-10-31 12:14:33.360228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '345fbdd1d04d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weight', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('height', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('height')
        batch_op.drop_column('weight')

    # ### end Alembic commands ###

"""added fields for questionairre

Revision ID: 9d5cf625bd40
Revises: fec29946cd59
Create Date: 2023-10-31 13:23:17.048705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d5cf625bd40'
down_revision = 'fec29946cd59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('birthday', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('activity_level', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('health_concerns', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('health_concerns')
        batch_op.drop_column('activity_level')
        batch_op.drop_column('birthday')
        batch_op.drop_column('gender')
        batch_op.drop_column('age')
        batch_op.drop_column('name')

    # ### end Alembic commands ###

"""Added new table model

Revision ID: d96cdf806e65
Revises: 9f256a7ade9e
Create Date: 2024-01-16 05:50:41.169123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd96cdf806e65'
down_revision = '9f256a7ade9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expert', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expert', schema=None) as batch_op:
        batch_op.drop_column('image_filename')

    # ### end Alembic commands ###

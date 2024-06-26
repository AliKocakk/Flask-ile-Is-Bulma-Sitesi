"""Added new table model

Revision ID: 6050018b6569
Revises: d96cdf806e65
Create Date: 2024-01-16 07:07:36.811606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6050018b6569'
down_revision = 'd96cdf806e65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application')
    # ### end Alembic commands ###

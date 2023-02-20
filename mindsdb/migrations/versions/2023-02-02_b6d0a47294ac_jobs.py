"""jobs

Revision ID: b6d0a47294ac
Revises: 459218b0844c
Create Date: 2023-02-02 11:33:06.283055

"""
from alembic import op
import sqlalchemy as sa
import mindsdb.interfaces.storage.db # noqa

# revision identifiers, used by Alembic.
revision = 'b6d0a47294ac'
down_revision = '459218b0844c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'jobs_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.Column('job_id', sa.Integer(), nullable=True),
        sa.Column('start_at', sa.DateTime(), nullable=True),
        sa.Column('end_at', sa.DateTime(), nullable=True),
        sa.Column('error', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('job_id', 'start_at', name='uniq_job_history_job_id_start')
    )
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('query_str', sa.String(), nullable=False),
        sa.Column('start_at', sa.DateTime(), nullable=True),
        sa.Column('end_at', sa.DateTime(), nullable=True),
        sa.Column('next_run_at', sa.DateTime(), nullable=True),
        sa.Column('schedule_str', sa.String(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs')
    op.drop_table('jobs_history')
    # ### end Alembic commands ###
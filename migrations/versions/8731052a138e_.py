"""Add details JSON column to user table.

Revision ID: 8731052a138e
Revises: 71477dadd6ef
Create Date: 2018-11-07 16:37:10.510120

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8731052a138e'
down_revision = '71477dadd6ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('details', postgresql.JSON(astext_type=sa.Text()), server_default='{"active_at": null}', nullable=True))


def downgrade():
    op.drop_column('users', 'details')

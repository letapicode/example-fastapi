"""add content column to posts table

Revision ID: 0196478763c4
Revises: 757baacaf5f1
Create Date: 2022-03-25 19:16:01.623041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0196478763c4'
down_revision = '757baacaf5f1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
    pass

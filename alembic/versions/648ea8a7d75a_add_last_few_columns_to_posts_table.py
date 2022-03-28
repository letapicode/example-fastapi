"""add last few columns to posts table

Revision ID: 648ea8a7d75a
Revises: 7ea6c3aacca9
Create Date: 2022-03-25 20:22:26.375904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '648ea8a7d75a'
down_revision = '7ea6c3aacca9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', 
                                     sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', 
                                     sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

"""add foreign-key to posts table

Revision ID: 7ea6c3aacca9
Revises: d365363a099b
Create Date: 2022-03-25 20:03:14.412501

"""
from threading import local
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea6c3aacca9'
down_revision = 'd365363a099b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

"""added has category helper table

Revision ID: 197acc8d4353
Revises: b8dd2d81b789
Create Date: 2022-06-04 08:50:00.909046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '197acc8d4353'
down_revision = 'b8dd2d81b789'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('has_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('has_categories')
    # ### end Alembic commands ###

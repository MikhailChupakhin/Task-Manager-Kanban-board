"""3.11 TM:правки_моделей

Revision ID: 38ad94012092
Revises: 0a78f65bad08
Create Date: 2023-11-03 14:29:11.137459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38ad94012092'
down_revision = '0a78f65bad08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('comment_count')

    # ### end Alembic commands ###

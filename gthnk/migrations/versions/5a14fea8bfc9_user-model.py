"""update user model to track last login info

Revision ID: 5a14fea8bfc9
Revises: fe4bd690134
Create Date: 2016-01-05 19:52:14.544778

"""

# revision identifiers, used by Alembic.
revision = '5a14fea8bfc9'
down_revision = 'fe4bd690134'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('current_login_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('current_login_ip', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('last_login_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('last_login_ip', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('login_count', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'login_count')
    op.drop_column('user', 'last_login_ip')
    op.drop_column('user', 'last_login_at')
    op.drop_column('user', 'current_login_ip')
    op.drop_column('user', 'current_login_at')
    ### end Alembic commands ###

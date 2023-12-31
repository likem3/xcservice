"""update users table

Revision ID: e3e37c119eab
Revises: 93b4bc22e1f9
Create Date: 2023-06-16 12:12:28.223709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3e37c119eab'
down_revision = '93b4bc22e1f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.Unicode(), nullable=False))
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('users', sa.Column('email_verified', sa.Boolean(), server_default='True', nullable=True))
    op.add_column('users', sa.Column('salt', sa.Unicode(), nullable=False))
    op.add_column('users', sa.Column('password', sa.Unicode(), nullable=False))
    op.add_column('users', sa.Column('is_active', sa.Boolean(), server_default='True', nullable=False))
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), server_default='False', nullable=False))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('users', 'nickname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nickname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'password')
    op.drop_column('users', 'salt')
    op.drop_column('users', 'email_verified')
    op.drop_column('users', 'email')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###

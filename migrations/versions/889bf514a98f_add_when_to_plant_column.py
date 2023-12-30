"""Add when_to_plant column

Revision ID: 889bf514a98f
Revises: e513945b7ec1
Create Date: 2023-12-29 23:03:40.995391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '889bf514a98f'
down_revision = 'e513945b7ec1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('when_to_plant', sa.String(length=300), nullable=True))
        batch_op.alter_column('scientific_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.alter_column('scientific_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.drop_column('when_to_plant')

    # ### end Alembic commands ###

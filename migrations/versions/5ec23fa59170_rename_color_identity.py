"""rename color_identity

Revision ID: 5ec23fa59170
Revises: 52460d58bb58
Create Date: 2024-10-02 13:11:34.275658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ec23fa59170'
down_revision = '52460d58bb58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('overlay', schema=None) as batch_op:
        batch_op.add_column(sa.Column('player1_commander1_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player1_commander2_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player2_commander1_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player2_commander2_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player3_commander1_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player3_commander2_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player4_commander1_ci', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('player4_commander2_ci', sa.String(), nullable=True))
        batch_op.drop_column('player3_commander2_color_identity')
        batch_op.drop_column('player3_commander1_color_identity')
        batch_op.drop_column('player2_commander1_color_identity')
        batch_op.drop_column('player2_commander2_color_identity')
        batch_op.drop_column('player4_commander1_color_identity')
        batch_op.drop_column('player1_commander1_color_identity')
        batch_op.drop_column('player4_commander2_color_identity')
        batch_op.drop_column('player1_commander2_color_identity')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('overlay', schema=None) as batch_op:
        batch_op.add_column(sa.Column('player1_commander2_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player4_commander2_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player1_commander1_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player4_commander1_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player2_commander2_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player2_commander1_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player3_commander1_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('player3_commander2_color_identity', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('player4_commander2_ci')
        batch_op.drop_column('player4_commander1_ci')
        batch_op.drop_column('player3_commander2_ci')
        batch_op.drop_column('player3_commander1_ci')
        batch_op.drop_column('player2_commander2_ci')
        batch_op.drop_column('player2_commander1_ci')
        batch_op.drop_column('player1_commander2_ci')
        batch_op.drop_column('player1_commander1_ci')

    # ### end Alembic commands ###

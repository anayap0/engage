"""Creating demo db file

Revision ID: bc616d599fc2
Revises: 005127b3d8ea
Create Date: 2021-03-17 11:17:40.153401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc616d599fc2'
down_revision = '005127b3d8ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(length=140), nullable=True),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('icon', sa.String(length=220), nullable=True),
    sa.Column('color', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_courses_code'), ['code'], unique=True)
        batch_op.create_index(batch_op.f('ix_courses_timestamp'), ['timestamp'], unique=False)

    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)

    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('timestamp_start', sa.DateTime(), nullable=True),
    sa.Column('timestamp_end', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_session_timestamp_end'), ['timestamp_end'], unique=False)
        batch_op.create_index(batch_op.f('ix_session_timestamp_start'), ['timestamp_start'], unique=False)

    op.create_table('signups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('course', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('signups', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_signups_timestamp'), ['timestamp'], unique=False)

    op.create_table('prompts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('form_question', sa.String(length=140), nullable=True),
    sa.Column('form_options', sa.Integer(), nullable=True),
    sa.Column('form_course_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['form_course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_prompts_timestamp'), ['timestamp'], unique=False)

    op.create_table('reactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('reactions', sa.Integer(), nullable=True),
    sa.Column('reactions_course_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['reactions_course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('reactions', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_reactions_timestamp'), ['timestamp'], unique=False)

    op.create_table('responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('form_prompt_id', sa.Integer(), nullable=True),
    sa.Column('form_responses', sa.Integer(), nullable=True),
    sa.Column('form_course_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['form_course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['form_prompt_id'], ['prompts.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('responses', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_responses_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('responses', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_responses_timestamp'))

    op.drop_table('responses')
    with op.batch_alter_table('reactions', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_reactions_timestamp'))

    op.drop_table('reactions')
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_prompts_timestamp'))

    op.drop_table('prompts')
    with op.batch_alter_table('signups', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_signups_timestamp'))

    op.drop_table('signups')
    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_session_timestamp_start'))
        batch_op.drop_index(batch_op.f('ix_session_timestamp_end'))

    op.drop_table('session')
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))

    op.drop_table('post')
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_courses_timestamp'))
        batch_op.drop_index(batch_op.f('ix_courses_code'))

    op.drop_table('courses')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
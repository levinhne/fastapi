"""initialize

Revision ID: 5bfabf9a5ea7
Revises: 
Create Date: 2024-11-17 12:43:58.207152

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

from alembic import op
from src.app.pipeline.domain.pipeline import Pipeline

# revision identifiers, used by Alembic.
revision: str = "5bfabf9a5ea7"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = Pipeline.__tablename__


def upgrade():
    op.create_table(
        table_name,
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("tenant_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("template_id", sa.Integer(), nullable=False),
        sa.Column("base_model_id", sa.Integer(), nullable=False),
        sa.Column("trainer_id", sa.Integer(), nullable=False),
        sa.Column(
            "data", JSONB(), nullable=False, server_default=sa.text("'{}'::jsonb")
        ),  # Default {}
        sa.Column("schedule", sa.String(length=255), nullable=True),
        sa.Column(
            "status",
            sa.Enum("New", "Running", "Completed", name="pipelinestatus"),
            nullable=False,
            default="New",
        ),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table(table_name)

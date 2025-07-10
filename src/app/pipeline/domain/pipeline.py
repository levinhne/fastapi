

from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from sqlalchemy import Column, event
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


class PipelineStatus(str, Enum):
    NEW = "New"
    RUNNING = "Running"
    COMPLETED = "Completed"


class Pipeline(SQLModel, table=True):

    __tablename__ = "pipelines"

    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: int = Field(nullable=False)
    user_id: int = Field(nullable=False)
    name: str = Field(max_length=255, nullable=False)
    template_id: int = Field(nullable=False)
    base_model_id: int = Field(nullable=False)
    trainer_id: int = Field(nullable=False)
    data: dict = Field(sa_column=Column(JSONB), default={})

    schedule: Optional[str] = Field(max_length=255, default=None)
    status: PipelineStatus = Field(default=PipelineStatus.NEW, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"onupdate": datetime.utcnow},
    )


@event.listens_for(Pipeline, "before_update", propagate=True)
def before_update(mapper, connection, target):
    """Update updated_at field before updating"""
    target.updated_at = datetime.now(timezone.utc)


@event.listens_for(Pipeline, "before_insert", propagate=True)
def before_insert(mapper, connection, target):
    """Update created_at field before inserting"""
    if not target.created_at:
        target.created_at = datetime.now(timezone.utc)

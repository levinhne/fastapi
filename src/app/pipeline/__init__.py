from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from src.app.pipeline.adapters.pipeline_repository import PipelineRepository
from src.app.pipeline.application.service import AbstractServiceApplication, Service
from src.core.database import Database


def get_sync_database() -> Database:
    return Database(
        "postgresql+psycopg://postgres:postgres@localhost:5432/pipelines", echo=True
    )


def get_service(db=Depends(get_sync_database)) -> AbstractServiceApplication:
    """Get Service"""
    pipeline_repository = PipelineRepository(session=db.session)
    return Service(repository=pipeline_repository)


__all__ = ["get_service"]

from sqlmodel import SQLModel

from src.app.pipeline.domain.pipeline import Pipeline

metadata = SQLModel.metadata

__all__ = ["metadata"]

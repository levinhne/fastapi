

from sqlalchemy.orm import scoped_session

from src.app.pipeline.application.ports.pipeline_repository import (
    AbstractPipelineRepository,
)
from src.app.pipeline.domain.pipeline import Pipeline


class PipelineRepository(AbstractPipelineRepository):
    """Pipeline Repository Class"""

    def __init__(self, session: scoped_session):
        self._session = session

    def get_pipeline_by_id(self, pipeline_id: int) -> Pipeline:
        with self._session() as session:
            return session.query(Pipeline).filter(Pipeline.id == pipeline_id).first()

    def create_pipeline(self, pipeline: Pipeline) -> Pipeline:
        with self._session() as session:
            try:
                session.add(pipeline)
                session.commit()
                session.refresh(pipeline)
            except Exception as e:
                raise RuntimeError(f"Database error: {e}")

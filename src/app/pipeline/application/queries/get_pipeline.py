from dataclasses import dataclass

from src.app.pipeline.application.queries.query import Query
from src.app.pipeline.domain.pipeline import Pipeline


@dataclass
class GetPipelineByID(Query):
    """Get pipeline by ID query."""

    pipeline_id: int


class GetPipelineHandler:
    """Get pipeline by ID handler."""

    def __init__(self, repository):
        self._repository = repository

    def handle(self, query: Query) -> Pipeline:
        """Handle get pipeline by ID query."""
        if isinstance(query, GetPipelineByID):
            return self._repository.get_pipeline_by_id(query.pipeline_id)

        raise ValueError("Query is not supported")

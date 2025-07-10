
"""Service Application Module"""

from abc import ABC, abstractmethod

from src.app.pipeline.application.queries.get_pipeline import GetPipelineHandler
from src.app.pipeline.application.queries.query import Query
from src.app.pipeline.domain.pipeline import Pipeline

from .ports import AbstractPipelineRepository


class Commands:
    """Commands Class"""

    def __init__(self, repository: AbstractPipelineRepository) -> None:
        pass


class Queries:
    """Queries Class"""

    def __init__(self, repository: AbstractPipelineRepository) -> None:
        self.get_pipeline_handler = GetPipelineHandler(repository)


class AbstractServiceApplication(ABC):
    """Service Application Abstract Class"""

    @abstractmethod
    def get_pipeline(self, query: Query) -> Pipeline:
        """Get Pipeline"""
        raise NotImplementedError

    @abstractmethod
    def create_pipeline(self, pipeline: Pipeline) -> None:
        """Create Pipeline"""
        raise NotImplementedError


class Service(AbstractServiceApplication):
    """Service Application Class"""

    def __init__(self, repository: AbstractPipelineRepository) -> None:
        self._commands = Commands(repository)
        self._queries = Queries(repository)

    def get_pipeline(self, query: Query) -> Pipeline:
        """Get Pipeline"""
        return self._queries.get_pipeline_handler.handle(query)

    def create_pipeline(self, pipeline: dict) -> dict:
        """Create Pipeline"""
        return pipeline

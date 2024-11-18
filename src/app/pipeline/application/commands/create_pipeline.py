from dataclasses import dataclass

from src.app.pipeline.domain.pipeline import Pipeline


@dataclass
class CreatePipelineCommand:
    pipeline: Pipeline


class CreatePipelineHandler:
    def __init__(self, repository):
        self._repository = repository

    def handle(self, command: CreatePipelineCommand):
        return self._repository.create_pipeline(command.pipeline)

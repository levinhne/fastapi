# -*- coding: utf-8 -*-
# Copyright (c) 2024, FPT Smart Cloud
# All rights reserved. Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.

from abc import ABC, abstractmethod

from src.app.pipeline.domain.pipeline import Pipeline


class AbstractPipelineRepository(ABC):
    """Pipeline Repository Abstract Class"""

    @abstractmethod
    def get_pipeline_by_id(self, pipeline_id: int) -> Pipeline:
        """Get Pipeline by ID"""
        raise NotImplementedError

    @abstractmethod
    def create_pipeline(self, pipeline: Pipeline) -> Pipeline:
        """Create Pipeline"""
        raise NotImplementedError

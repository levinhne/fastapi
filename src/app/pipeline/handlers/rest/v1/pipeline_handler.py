

from fastapi import APIRouter, Depends, HTTPException, status

from src.app.pipeline import get_service
from src.app.pipeline.application.queries.get_pipeline import GetPipelineByID
from src.app.pipeline.application.service import AbstractServiceApplication
from src.app.pipeline.domain.pipeline import Pipeline
from src.core.response import ResponseSchema, success_response

router = APIRouter(prefix="/v1/pipelines", tags=["pipelines"])


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class PipelineStatus(str, Enum):
    NEW = "New"
    RUNNING = "Running"
    COMPLETED = "Completed"


# Request and Response Models
class PipelineDataDatasetRequest(BaseModel):
    training_data_id: str
    evaluation_data_id: str
    evaluation_data_percentage_of_split: int
    test_data_id: str
    preprocessing_steps: Optional[List[Dict[str, Any]]]
    augmentation: Optional[Dict[str, Any]]


class PipelineDataHyperparametersRequest(BaseModel):
    epochs: int
    batch_size: int
    learning_rate: float
    sequence_length: int
    save_steps: int
    gradient_accumulation_steps: int
    optimizer: str
    scheduler: Optional[Dict[str, Any]]


class PipelineDataRequest(BaseModel):
    dataset: PipelineDataDatasetRequest
    hyperparameters: PipelineDataHyperparametersRequest
    infrastructure: Optional[str]
    instance_flavor: Optional[str]
    number_of_checkpoint: int
    checkpoint_interval: int
    auto_deployment_to_serving: bool
    notifications: Optional[List[Dict[str, str]]]
    publish_event: Optional[List[Dict[str, Any]]]


class PipelineRequest(BaseModel):
    tenant_id: int
    user_id: int
    name: str
    template_id: int
    base_model_id: int
    trainer_id: int
    data: PipelineDataRequest
    schedule: Optional[str]
    status: Optional[PipelineStatus] = PipelineStatus.NEW


class PipelineResponse(BaseModel):
    id: int
    tenant_id: int
    user_id: int
    name: str
    template_id: int
    base_model_id: int
    trainer_id: int
    data: PipelineDataRequest
    schedule: Optional[str]
    status: PipelineStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


@router.post("")
def create_pipeline(pipeline: PipelineRequest):
    return {}


@router.get("/{pipeline_id}", response_model=ResponseSchema[Pipeline])
def get_pipeline_by_id(
    pipeline_id: int, app: AbstractServiceApplication = Depends(get_service)
):
    """Get pipeline by ID"""
    pipeline = app.get_pipeline(GetPipelineByID(pipeline_id=pipeline_id))
    if not pipeline:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pipeline {pipeline_id} not found",
        )
    return success_response(
        data=app.get_pipeline(GetPipelineByID(pipeline_id=pipeline_id)),
        message="Get pipeline by ID",
    )


@router.get("", response_model=ResponseSchema[dict])
def list_pipelines(app: AbstractServiceApplication = Depends(get_service)):
    """List all pipelines"""

    return success_response(
        data=app.create_pipeline({"Hello": "World"}), message="List all pipelines"
    )

from fastapi import FastAPI

from src.app.pipeline.handlers.rest.v1 import router as pipeline_router

app = FastAPI()

app.include_router(pipeline_router)

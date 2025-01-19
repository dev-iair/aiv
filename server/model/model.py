from pydantic import BaseModel
from datetime import datetime
from database.model import Model, ModelVersion


class CreateModelRequests(BaseModel):
    name: str
    version: str


class CreateModelResponse(BaseModel):
    model: Model
    model_version: ModelVersion


class ModelWithVersions(BaseModel):
    model: Model
    model_versions: list[ModelVersion]


class GetModelResponse(BaseModel):
    models: list[ModelWithVersions]


class UpdateModelRequests(BaseModel):
    id: int
    name: str


class UpdateModelResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime | None


class CreateModelVersionRequests(BaseModel):
    model_id: int
    version: str


class CreateModelVersionResponse(BaseModel):
    id: int
    model_id: int
    version: str
    created_at: datetime
    updated_at: datetime | None


class GetModelVersionResponse(BaseModel):
    id: int
    model_id: int
    version: str
    created_at: datetime
    updated_at: datetime | None

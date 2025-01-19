from pydantic import BaseModel
from datetime import datetime
from database.model import ModelTrain, ModelTrainParameter


class CreateModelTrainRequests(BaseModel):
    model_version_id: int
    version: str
    status: str
    params: list[dict[str, str]]


class CreateModelTrainResponse(BaseModel):
    id: int
    model_version_id: int
    version: str
    status: str
    created_at: datetime
    updated_at: datetime | None


class ModelTrainWithParameters(BaseModel):
    model_train: ModelTrain
    parameters: list[ModelTrainParameter]


class GetModelTrainResponse(BaseModel):
    model_trains: list[ModelTrainWithParameters]

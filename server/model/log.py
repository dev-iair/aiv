from pydantic import BaseModel
from datetime import datetime
from database.model import Log


class SetLogRequests(BaseModel):
    model_train_id: int
    type: str
    message: str


class SetLogResponse(BaseModel):
    id: int
    model_train_id: int
    type: str
    message: str
    created_at: datetime


class GetLogsRequests(BaseModel):
    model_train_id: int
    type: str


class GetLogsResponse(BaseModel):
    logs: list[Log]

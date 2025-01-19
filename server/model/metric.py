from pydantic import BaseModel
from datetime import datetime
from database.model import Metric


class SetMetricRequests(BaseModel):
    model_train_id: int
    epoch: int
    step: int | None
    phase: str | None
    name: str
    value: float


class SetMetricResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime | None
    model_train_id: int
    epoch: int
    step: int | None
    phase: str | None
    name: str
    value: float


class GetMetricResponse(BaseModel):
    metrics: list[Metric]

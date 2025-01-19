from pydantic import BaseModel
from datetime import datetime
from database.model import Artifact


class SetArtifactRequests(BaseModel):
    model_train_id: int
    type: str
    file_path: str
    file_size: int
    epoch: int
    step: int | None
    phase: str | None


class SetArtifactResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime | None
    model_train_id: int
    type: str
    file_path: str
    file_size: int
    epoch: int
    step: int | None
    phase: str | None


class GetArtifactResponse(BaseModel):
    artifacts: list[Artifact]

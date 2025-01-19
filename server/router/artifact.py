from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from typing import Annotated
from database.database import get_session
import model.artifact as artifact_model
import service.artifact as artifact_service

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/")
def set_artifact(
    req_data: artifact_model.SetArtifactRequests, session: SessionDep
) -> artifact_model.SetArtifactResponse:
    artifact_check = artifact_service.check_artifact(session, req_data)
    if artifact_check:
        artifact = artifact_service.update_artifact(session, req_data, artifact_check)
    else:
        artifact = artifact_service.set_artifact(session, req_data)
    res = artifact_model.SetArtifactResponse(
        model_train_id=artifact.model_train_id,
        id=artifact.id,
        type=artifact.type,
        file_path=artifact.file_path,
        file_size=artifact.file_size,
        epoch=artifact.epoch,
        step=artifact.step,
        phase=artifact.phase,
        created_at=artifact.created_at,
        updated_at=artifact.updated_at,
    )
    return res


@router.get("/")
def get_artifact(
    session: SessionDep,
    model_train_id: int,
    type: str | None = None,
    epoch: int | None = None,
    step: int | None = None,
    phase: str | None = None,
) -> artifact_model.GetArtifactResponse:
    artifacts = artifact_service.get_artifacts(
        session,
        model_train_id,
        type,
        epoch,
        step,
        phase,
    )
    res = artifact_model.GetArtifactResponse(artifacts=artifacts)
    return res

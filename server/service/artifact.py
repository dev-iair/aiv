from sqlmodel import Session, select
from model.artifact import SetArtifactRequests
from database.model import *


def check_artifact(session: Session, req_data: SetArtifactRequests) -> Artifact:
    statement = select(Artifact).where(
        (Artifact.model_train_id == req_data.model_train_id)
        & (Artifact.type == req_data.type)
        & (Artifact.epoch == req_data.epoch)
        & (Artifact.step == req_data.step)
        & (Artifact.phase == req_data.phase)
    )
    artifact = session.exec(statement).first()
    return artifact


def update_artifact(
    session: Session, req_data: SetArtifactRequests, artifact: Artifact
) -> Artifact:
    artifact.file_path = req_data.file_path
    artifact.file_size = req_data.file_size
    session.add(artifact)
    session.commit()
    session.refresh(artifact)
    return artifact


def set_artifact(session: Session, req_data: SetArtifactRequests) -> Artifact:
    artifact = Artifact(
        model_train_id=req_data.model_train_id,
        type=req_data.type,
        file_path=req_data.file_path,
        file_size=req_data.file_size,
        epoch=req_data.epoch,
        step=req_data.step,
        phase=req_data.phase,
    )
    session.add(artifact)
    session.commit()
    session.refresh(artifact)
    return artifact


def get_artifacts(
    session: Session,
    model_train_id: int,
    artifact_type: str | None = None,
    artifact_epoch: int | None = None,
    artifact_step: int | None = None,
    artifact_phase: str | None = None,
) -> list[Artifact]:
    statement = select(Artifact).where(Artifact.model_train_id == model_train_id)
    if artifact_type:
        statement = statement.where(Artifact.type == artifact_type)
    if artifact_epoch:
        statement = statement.where(Artifact.epoch == artifact_epoch)
    if artifact_step:
        statement = statement.where(Artifact.step == artifact_step)
    if artifact_phase:
        statement = statement.where(Artifact.phase == artifact_phase)
    artifacts = session.exec(statement).all()
    return artifacts

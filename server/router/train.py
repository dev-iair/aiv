from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlmodel import Session
from typing import Annotated
from database.database import get_session
import model.train as train_model
import service.train as train_service

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/")
def set_train(
    req_data: train_model.CreateModelTrainRequests, session: SessionDep
) -> train_model.CreateModelTrainResponse:

    train_data = train_service.check_train_with_version(
        req_data.model_version_id, req_data.version, session
    )

    if train_data:
        raise HTTPException(
            status_code=400, detail="Model train version already exists"
        )
    else:
        train_data = train_service.create_model_train(
            req_data.model_version_id,
            req_data.version,
            req_data.status,
            req_data.params,
            session,
        )

    res = train_model.CreateModelTrainResponse(
        id=train_data.id,
        model_version_id=train_data.model_version_id,
        version=train_data.version,
        status=train_data.status,
        created_at=train_data.created_at,
        updated_at=train_data.updated_at,
    )

    return res


@router.get("/")
def get_train(
    session: SessionDep, model_version_id: int
) -> train_model.GetModelTrainResponse:
    train_data = train_service.get_model_train_with_parameters(
        model_version_id, session
    )

    res = train_model.GetModelTrainResponse(model_trains=train_data)

    return res

from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from typing import Annotated
from database.database import get_session
import model.log as log_model
import service.log as log_service

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/")
def set_log(
    req_data: log_model.SetLogRequests, session: SessionDep
) -> log_model.SetLogResponse:
    log = log_service.set_log(session, req_data)
    res = log_model.SetLogResponse(
        id=log.id,
        model_train_id=log.model_train_id,
        type=log.type,
        message=log.message,
        created_at=log.created_at,
    )
    return res


@router.get("/")
def get_logs(
    session: SessionDep, model_train_id: int, type: str | None = None
) -> log_model.GetLogsResponse:
    logs = log_service.get_logs(session, model_train_id, type)
    res = log_model.GetLogsResponse(
        logs=logs,
    )
    print(res)
    return res

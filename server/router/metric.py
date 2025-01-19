from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session
from typing import Annotated
from database.database import get_session
import model.metric as metric_model
import service.metric as metric_service

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/")
def set_metric(
    req_data: metric_model.SetMetricRequests, session: SessionDep
) -> metric_model.SetMetricResponse:
    metric_check = metric_service.check_metric(session, req_data)
    if metric_check:
        metric = metric_service.update_metric(session, req_data, metric_check)
    else:
        metric = metric_service.set_metric(session, req_data)
    res = metric_model.SetMetricResponse(
        id=metric.id,
        model_train_id=metric.model_train_id,
        name=metric.name,
        value=metric.value,
        epoch=metric.epoch,
        step=metric.step,
        phase=metric.phase,
        created_at=metric.created_at,
        updated_at=metric.updated_at,
    )
    return res


@router.get("/")
def get_metric(
    session: SessionDep,
    model_train_id: int,
    name: str | None = None,
    epoch: int | None = None,
    step: int | None = None,
    phase: str | None = None,
) -> metric_model.GetMetricResponse:
    metrics = metric_service.get_metrics(
        session, model_train_id, name, epoch, step, phase
    )
    res = metric_model.GetMetricResponse(metrics=metrics)
    return res

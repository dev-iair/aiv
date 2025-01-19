from sqlmodel import Session, select
from model.metric import SetMetricRequests
from database.model import *


def check_metric(session: Session, metric_data: SetMetricRequests) -> bool:
    statement = select(Metric).where(
        (Metric.model_train_id == metric_data.model_train_id)
        & (Metric.name == metric_data.name)
        & (Metric.epoch == metric_data.epoch)
        & (Metric.phase == metric_data.phase)
        & (Metric.step == metric_data.step)
    )
    metric = session.exec(statement).first()
    return metric


def set_metric(session: Session, metric_data: SetMetricRequests) -> Metric:
    metric = Metric(
        model_train_id=metric_data.model_train_id,
        name=metric_data.name,
        value=metric_data.value,
        epoch=metric_data.epoch,
        phase=metric_data.phase,
        step=metric_data.step,
    )
    session.add(metric)
    session.commit()
    session.refresh(metric)
    return metric


def update_metric(
    session: Session, metric_data: SetMetricRequests, metric: Metric
) -> Metric:
    metric.value = metric_data.value
    session.add(metric)
    session.commit()
    session.refresh(metric)
    return metric


def get_metrics(
    session: Session,
    model_train_id: int,
    metric_name: str | None = None,
    metric_epoch: int | None = None,
    metric_step: int | None = None,
    metric_phase: str | None = None,
) -> list[Metric]:
    statement = select(Metric).where(Metric.model_train_id == model_train_id)
    if metric_name:
        statement = statement.where(Metric.name == metric_name)
    if metric_epoch:
        statement = statement.where(Metric.epoch == metric_epoch)
    if metric_step:
        statement = statement.where(Metric.step == metric_step)
    if metric_phase:
        statement = statement.where(Metric.phase == metric_phase)
    metrics = session.exec(statement).all()
    return metrics

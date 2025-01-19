from sqlmodel import Session, select
from model.log import SetLogRequests
from database.model import *


def set_log(session: Session, req_data: SetLogRequests) -> Log:
    log = Log(
        model_train_id=req_data.model_train_id,
        type=req_data.type,
        message=req_data.message,
    )
    session.add(log)
    session.commit()
    session.refresh(log)
    return log


def get_logs(session: Session, model_train_id: int, log_type: str = None) -> list[Log]:

    statement = select(Log).where(Log.model_train_id == model_train_id)
    if log_type:
        statement = statement.where(Log.type == log_type)
    logs = session.exec(statement).all()
    return logs

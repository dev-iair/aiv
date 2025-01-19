from sqlmodel import Session, select
from model.train import *
from database.model import *


def check_train_with_version(model_version_id: int, version: str, session: Session):
    statement = (
        select(ModelTrain)
        .where(ModelTrain.model_version_id == model_version_id)
        .where(ModelTrain.version == version)
    )
    result = session.exec(statement)
    db_model_train = result.first()
    return db_model_train


def create_model_train(
    model_version_id: int,
    version: str,
    status: str,
    params: list[dict],
    session: Session,
):
    db_model_train = ModelTrain(
        model_version_id=model_version_id, version=version, status=status
    )
    session.add(db_model_train)
    session.commit()
    session.refresh(db_model_train)

    for param in params:
        get_key = None
        get_value = None
        for key, value in param.items():
            get_key = key
            get_value = value
        db_model_train_param = ModelTrainParameter(
            model_train_id=db_model_train.id,
            name=get_key,
            value=get_value,
        )
        session.add(db_model_train_param)
        session.commit()
        session.refresh(db_model_train_param)

    return db_model_train


def get_model_train_with_parameters(model_version_id: int, session: Session):
    statement = select(ModelTrain).where(
        ModelTrain.model_version_id == model_version_id
    )
    db_model_train = session.exec(statement).all()
    model_train_with_parameters = []
    for train in db_model_train:
        statement = select(ModelTrainParameter).where(
            ModelTrainParameter.model_train_id == train.id
        )
        db_model_train_parameters = session.exec(statement).all()
        model_train_with_parameters.append(
            ModelTrainWithParameters(
                model_train=train, parameters=db_model_train_parameters
            )
        )
    return model_train_with_parameters

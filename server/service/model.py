from sqlmodel import Session, select
from model.model import *
from database.model import *


def create_model(model_name, session: Session):
    db_model = Model(name=model_name)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


def get_model(model_id: int, session: Session):
    statement = select(Model).where(Model.id == model_id)
    result = session.exec(statement)
    db_model = result.first()
    return db_model


def get_model_with_versions(model_id: int, session: Session):
    statement = (
        select(Model, ModelVersion)
        .join(ModelVersion, Model.id == ModelVersion.model_id)
        .where(Model.id == model_id)
    )
    result = session.exec(statement)
    db_model = result.all()
    return db_model


def get_models(session: Session):
    statement = select(Model)
    result = session.exec(statement)
    db_models = result.all()
    return db_models


def get_model_with_name(model_name: str, session: Session):
    statement = select(Model).where(Model.name == model_name)
    result = session.exec(statement)
    db_model = result.first()
    return db_model


def update_model(model: UpdateModelRequests, session: Session):
    db_model = session.get(Model, model.id)
    db_model.name = model.name
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


def create_model_version(model_id, model_version, session: Session):
    db_model_version = ModelVersion(model_id=model_id, version=model_version)
    session.add(db_model_version)
    session.commit()
    session.refresh(db_model_version)
    return db_model_version


def get_model_version(model_version_id: int, session: Session):
    statement = select(ModelVersion).where(ModelVersion.id == model_version_id)
    result = session.exec(statement)
    db_model_version = result.first()
    return db_model_version


def get_model_version_with_version(model_id: int, model_version: str, session: Session):
    statement = (
        select(ModelVersion)
        .where(ModelVersion.model_id == model_id)
        .where(ModelVersion.version == model_version)
    )
    result = session.exec(statement)
    db_model_version = result.first()
    return db_model_version

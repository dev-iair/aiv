from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlmodel import Session
from typing import Annotated
from database.database import get_session
from model.model import Model, ModelVersion
import model.model as model_model
import service.model as model_service

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/")
def set_model(
    req_data: model_model.CreateModelRequests, session: SessionDep
) -> model_model.CreateModelResponse:

    res = model_model.CreateModelResponse

    model = model_service.get_model_with_name(req_data.name, session)

    if model:
        res.model = model.model_copy()
        model_version = model_service.get_model_version_with_version(
            model.id, req_data.version, session
        )
        if model_version:
            res.model_version = model_version.model_copy()
        else:
            model_version = model_service.create_model_version(
                model.id, req_data.version, session
            )
            res.model_version = model_version.model_copy()
    else:
        model = model_service.create_model(req_data.name, session)
        res.model = model.model_copy()
        model_version = model_service.create_model_version(
            model.id, req_data.version, session
        )
        res.model_version = model_version.model_copy()

    return res


@router.get("/")
def get_model(model_id: int, session: SessionDep) -> model_model.GetModelResponse:

    model = model_service.get_model_with_versions(model_id, session)
    res = model_model.GetModelResponse(
        models=[
            model_model.ModelWithVersions(
                model=model[0][0],
                model_versions=[model_version[1] for model_version in model],
            )
        ]
    )
    return res


@router.get("/list")
def get_model_list(session: SessionDep) -> list[Model]:

    res = []

    models = model_service.get_models(session)

    for model in models:
        res.append(model.model_copy())

    return res

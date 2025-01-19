from sqlmodel import Field, SQLModel, UniqueConstraint, func, Column, DateTime
from datetime import datetime


class Model(SQLModel, table=True):
    __tablename__ = "model"
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    name: str = Field(default=None, unique=True)


class ModelVersion(SQLModel, table=True):
    __tablename__ = "model_version"
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    model_id: int = Field(default=None, foreign_key="model.id")
    version: str = Field(default=None)

    __table_args__ = (UniqueConstraint("model_id", "version"),)


class ModelTrain(SQLModel, table=True):
    __tablename__ = "model_train"
    id: int = Field(default=None, primary_key=True)
    version: str = Field(default=None)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    model_version_id: int = Field(default=None, foreign_key="model_version.id")
    status: str = Field(default=None)

    __table_args__ = (UniqueConstraint("model_version_id", "version"),)


class ModelTrainParameter(SQLModel, table=True):
    __tablename__ = "model_train_parameter"
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    model_train_id: int = Field(default=None, foreign_key="model_train.id")
    name: str = Field(default=None)
    value: str = Field(default=None)

    __table_args__ = (UniqueConstraint("model_train_id", "name"),)


class Artifact(SQLModel, table=True):
    __tablename__ = "artifact"
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    model_train_id: int = Field(default=None, foreign_key="model_train.id")
    type: str = Field(default=None)
    file_path: str = Field(default=None)
    file_size: int = Field(default=None)
    epoch: int = Field(default=None)
    step: int = Field(default=None)
    phase: str = Field(default=None)

    __table_args__ = (UniqueConstraint("model_train_id", "type"),)


class Log(SQLModel, table=True):
    __tablename__ = "log"
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    model_train_id: int = Field(default=None, foreign_key="model_train.id")
    type: str = Field(default=None)
    message: str = Field(default=None)


class Metric(SQLModel, table=True):
    __tablename__ = "metric"
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime, default=func.now()))
    updated_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    model_train_id: int = Field(default=None, foreign_key="model_train.id")
    epoch: int = Field(default=None)
    step: int = Field(default=None)
    phase: str = Field(default=None)
    name: str = Field(default=None)
    value: float = Field(default=None)

    __table_args__ = (UniqueConstraint("model_train_id", "epoch", "name", "phase"),)

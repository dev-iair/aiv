from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import router.metric as metric_router
import router.model as model_router
import router.train as train_router
import router.artifact as artifact_router
import router.log as log_router
from database.database import engine
from sqlmodel import SQLModel

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(train_router.router, prefix="/api/train", tags=["train"])
app.include_router(model_router.router, prefix="/api/model", tags=["model"])
app.include_router(artifact_router.router, prefix="/api/artifact", tags=["artifact"])
app.include_router(metric_router.router, prefix="/api/metric", tags=["metric"])
app.include_router(log_router.router, prefix="/api/log", tags=["log"])


@app.on_event("startup")
async def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/api/health", tags=["health"])
async def health():
    return {"status": "ok"}

from contextlib import asynccontextmanager

from config.settings import settings
from database.init_sqlite import init_db
from fastapi import FastAPI
from routes import api_router, user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("BEFORE START")
    print("DB INIT START")
    init_db()
    yield
    print("AFTER END")


if settings.env == "production":
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        lifespan=lifespan
    )
else:
    app = FastAPI(lifespan=lifespan)


app.include_router(api_router.router, prefix="/api", tags=["API"])
app.include_router(user_router.router, prefix="/users", tags=["User"])

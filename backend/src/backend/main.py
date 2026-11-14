
from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.shared import db_conn
from backend.shared.config_env import DB_URL


#routers

from backend.controller.routes import router_urls


@asynccontextmanager
async def lifespan(fast_api:FastAPI): 
    db_conn.DB_POOL.open()
    db_conn.DB_POOL.wait(timeout=1)
    yield
    db_conn.DB_POOL.close()

app =  FastAPI(lifespan=lifespan)

app.include_router(router_urls)
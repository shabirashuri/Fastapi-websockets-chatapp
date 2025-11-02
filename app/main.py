from fastapi import FastAPI # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from .routers import chat # type: ignore
from .database import engine, Base
import asyncio

app = FastAPI()
app.include_router(chat.router)

html = open("app/templates/index.html").read()

@app.get("/")
def get():
    return HTMLResponse(html)

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

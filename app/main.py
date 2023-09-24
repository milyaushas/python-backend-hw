from fastapi import FastAPI

from app.routers import router

app = FastAPI(
    title="App",
    description="Simple FastAPI app",
    version="0.0.1",
    docs_url="/docs"
)

app.include_router(router)
from fastapi import FastAPI

from app.routers import router

app = FastAPI(
    title="Library App",
    description="App created to store and update data about library members and books",
    version="0.0.1",
    docs_url="/docs",
)

app.include_router(router)

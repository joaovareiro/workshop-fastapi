from fastapi import FastAPI
from .routes import main_router

app = FastAPI(
    title="microblog",
    version="0.1.0",
    description="microblog is a posting app to clone twitter",
)

app.include_router(main_router)

from fastapi import FastAPI

app = FastAPI(
    title="microblog",
    version="0.1.0",
    description="microblog is a posting app to clone twitter",
)


@app.get("/")
async def index():
    return {"hello": "world"}

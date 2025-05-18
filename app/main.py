from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz", tags=["system"])
async def healthz():
    return {"status": "ok"}


@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(prefix="/api")

@app.get("/test")
async def test():
    return {"message": "Hello World"}

class TestRequest(BaseModel):
    key: str

@app.post("/test")
async def test_post(payload: TestRequest):
    if payload.key == "cxcxc":
        return {"message": "Success"}
    else:
        return {"message": "Failed"}


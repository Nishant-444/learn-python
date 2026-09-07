import fastapi
from fastapi import UploadFile
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def home():
    return {"data": "hello world"}


@app.get("/contact")
def contact():
    return {"data": "9876543210"}


@app.post("/upload")
def handleImage(files: UploadFile):
    print(files)
    return {"status": "received the files"}


if __name__ == "__main__":
    uvicorn.run(app)

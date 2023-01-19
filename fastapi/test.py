import typing

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/uploadfiles/")
def create_upload_files(files: typing.List[UploadFile] = File(...)):
    for file in files:
        with open(file.filename, "wb") as myfile:
            content = file.read()
            myfile.write(content)
        return "Hecho"


@app.get("/")
def index():
    return "Hello"

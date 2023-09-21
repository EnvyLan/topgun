# This is a sample Python script.

import os
import uuid

from fastapi import FastAPI, UploadFile, Response
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from topgun.models.ExecuteModel import ExecuteModel
from topgun.nlphandler import find_top1
from topgun.ocr import extract_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/execute")
def execute(item: ExecuteModel, response: Response):
    try:
        workflow, scope = find_top1(item.words)
        file_list = item.file_list
        data = extract_data(file_list)
        return {"msg": f"will execute {workflow}, match_scopt: {scope}", "file_data": data}
    except Exception as e:
        response.status_code = 400
        return {"msg": str(e), "error_code": "400"}


@app.post("/upload/")
async def upload_file(file: UploadFile):
    print("yes")
    file_byte = file.file.read()
    file_name = file.filename
    if not os.path.exists("upload"):
        os.mkdir("upload")
    with open(f"upload/{file_name}", 'wb') as f:
        f.write(file_byte)
    return {"file_path": f"upload/{uuid.uuid4()}/{file_name}"}


@app.get("/index", response_class=HTMLResponse)
def index():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look TopGun!</h1>
        </body>
    </html>
    """

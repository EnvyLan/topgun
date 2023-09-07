# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(root_path="/hello-azure/")


@app.get('/hello')
def root(request: Request):
    return {"hello": "azure", "root": request.scope.get("root_path")}


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
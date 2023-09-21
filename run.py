from topgun.main import app
from uvicorn import run

run(app, port=3000, host="0.0.0.0")
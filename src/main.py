import uvicorn
from fastapi import FastAPI

from application import create_app

app: FastAPI = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)

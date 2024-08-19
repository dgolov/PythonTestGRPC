from connections.grpc_server import serve
from fastapi import FastAPI
from routes import routes

import uvicorn
import threading


app = FastAPI()
app.include_router(routes)


@app.on_event("startup")
def startup_event():
    threading.Thread(target=serve).start()


if __name__ == "__main__":
    print("Start FastAPI app for testing gRPC")
    uvicorn.run(app, host="127.0.0.1", port=8000)


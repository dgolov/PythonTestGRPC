from connections.grpc_server import serve
from fastapi import FastAPI
from routes import routes

app = FastAPI()
app.include_router(routes)


@app.on_event("startup")
def startup_event():
    import threading
    threading.Thread(target=serve).start()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


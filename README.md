# Fast API gRPS Example

Install requirements

```bash
pip install -r requirements.txt
```

Generate code by proto file

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protos/*.proto
```

Run FastAPI app

```bash
uvicorn main.py:app
```

Run client
```bash
python ./client/client.py
```

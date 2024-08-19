# client.py
import grpc
from protos import service_pb2, service_pb2_grpc
from setings import HOST, PORT


def run():
    channel = grpc.insecure_channel(f"{HOST}:{PORT}")
    stub = service_pb2_grpc.HelloWorldStub(channel)
    response = stub.SayHello(service_pb2.HelloRequest(name='world'))
    print(f"Received: {response.message}")


if __name__ == '__main__':
    run()

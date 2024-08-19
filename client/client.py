# client.py
import grpc
from protos import service_pb2, service_pb2_grpc


def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = service_pb2_grpc.HelloWorldStub(channel)
    response = stub.SayHello(service_pb2.HelloRequest(name='world'))
    print(f"Received: {response.message}")


if __name__ == '__main__':
    run()

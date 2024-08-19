import grpc
from concurrent import futures
from protos import service_pb2, service_pb2_grpc


class HelloWorldServicer(service_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        print(f"SayHello request - {request}")
        return service_pb2.HelloReply(message=f"Hello, {request.name}!")


def serve():
    print("Start gRPC server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

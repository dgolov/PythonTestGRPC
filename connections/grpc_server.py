import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc


class HelloWorldServicer(service_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        print(request)
        return service_pb2.HelloReply(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

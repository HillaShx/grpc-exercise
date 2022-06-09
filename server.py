import logging
from concurrent import futures

import grpc

import main_pb2
import main_pb2_grpc


class gRPCExerciseServicer(main_pb2_grpc.gRPCExerciseServicer):
    def add2Numbers(self, request, context):
        return main_pb2.Result(result=request.elmt1 + request.elmt2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_gRPCExerciseServicer_to_server(
      gRPCExerciseServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

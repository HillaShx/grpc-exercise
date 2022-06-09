# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import main_pb2 as main__pb2


class gRPCExerciseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add2Numbers = channel.unary_unary(
                '/gRPCExercise/add2Numbers',
                request_serializer=main__pb2.Elements.SerializeToString,
                response_deserializer=main__pb2.Result.FromString,
                )


class gRPCExerciseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add2Numbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_gRPCExerciseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add2Numbers': grpc.unary_unary_rpc_method_handler(
                    servicer.add2Numbers,
                    request_deserializer=main__pb2.Elements.FromString,
                    response_serializer=main__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gRPCExercise', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class gRPCExercise(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add2Numbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gRPCExercise/add2Numbers',
            main__pb2.Elements.SerializeToString,
            main__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

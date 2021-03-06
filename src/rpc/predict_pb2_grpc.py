# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rpc.predict_pb2 as predict__pb2


class PredictionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.doPrediction = channel.unary_unary(
                '/PredictionService/doPrediction',
                request_serializer=predict__pb2.PredictRequest.SerializeToString,
                response_deserializer=predict__pb2.PredictResponse.FromString,
                )


class PredictionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def doPrediction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'doPrediction': grpc.unary_unary_rpc_method_handler(
                    servicer.doPrediction,
                    request_deserializer=predict__pb2.PredictRequest.FromString,
                    response_serializer=predict__pb2.PredictResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PredictionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PredictionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def doPrediction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PredictionService/doPrediction',
            predict__pb2.PredictRequest.SerializeToString,
            predict__pb2.PredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

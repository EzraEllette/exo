# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import node_service_pb2 as node__service__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in node_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class NodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendPrompt = channel.unary_unary(
                '/node_service.NodeService/SendPrompt',
                request_serializer=node__service__pb2.PromptRequest.SerializeToString,
                response_deserializer=node__service__pb2.Tensor.FromString,
                _registered_method=True)
        self.SendTensor = channel.unary_unary(
                '/node_service.NodeService/SendTensor',
                request_serializer=node__service__pb2.TensorRequest.SerializeToString,
                response_deserializer=node__service__pb2.Tensor.FromString,
                _registered_method=True)
        self.ResetShard = channel.unary_unary(
                '/node_service.NodeService/ResetShard',
                request_serializer=node__service__pb2.ResetShardRequest.SerializeToString,
                response_deserializer=node__service__pb2.Empty.FromString,
                _registered_method=True)


class NodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendPrompt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTensor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetShard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendPrompt': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPrompt,
                    request_deserializer=node__service__pb2.PromptRequest.FromString,
                    response_serializer=node__service__pb2.Tensor.SerializeToString,
            ),
            'SendTensor': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTensor,
                    request_deserializer=node__service__pb2.TensorRequest.FromString,
                    response_serializer=node__service__pb2.Tensor.SerializeToString,
            ),
            'ResetShard': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetShard,
                    request_deserializer=node__service__pb2.ResetShardRequest.FromString,
                    response_serializer=node__service__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'node_service.NodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('node_service.NodeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendPrompt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/node_service.NodeService/SendPrompt',
            node__service__pb2.PromptRequest.SerializeToString,
            node__service__pb2.Tensor.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendTensor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/node_service.NodeService/SendTensor',
            node__service__pb2.TensorRequest.SerializeToString,
            node__service__pb2.Tensor.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetShard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/node_service.NodeService/ResetShard',
            node__service__pb2.ResetShardRequest.SerializeToString,
            node__service__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

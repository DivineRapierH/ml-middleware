import logging

import grpc
import tensorflow as tf
from numpy import ndarray
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

from config import TF_RPC_SERVER

log = logging.getLogger(__name__)


def predictCirProb(data: ndarray) -> float:
    with grpc.insecure_channel(TF_RPC_SERVER) as channel:
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        predictRequest = predict_pb2.PredictRequest()
        predictRequest.model_spec.name = 'cir_classify_01_model'
        predictRequest.model_spec.signature_name = 'serving_default'
        predictRequest.inputs['book_embedding_input'].CopyFrom(tf.make_tensor_proto(data))
        result = stub.Predict(predictRequest, 60)
        log.debug(result)
        return result.outputs['cir_prob'].float_val[1]


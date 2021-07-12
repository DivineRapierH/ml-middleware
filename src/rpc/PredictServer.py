import grpc
import numpy as np
from concurrent import futures

import rpc.predict_pb2_grpc as predict_pb2_grpc
import rpc.predict_pb2 as predict_pb2
from rpc.TFAccess import predictCirProb
from shared.HanLPAPI import annotate, extractTag
from shared.common import ft


def predict(strList: list[str]) -> float:
    embedding = calcEmbedding(strList)
    return predictCirProb(np.array([embedding], dtype='float64'))


def calcEmbedding(strList: list[str]) -> np.ndarray:
    tagListList = extractTag(annotate(strList))
    tagNameSet = set()
    for tagList in tagListList:
        for tag in tagList:
            tagNameSet.add(tag.name)
    embedding = np.average(np.array(list(map(lambda name: ft.get_word_vector(name),
                                             filter(lambda name: name is not None and len(name) > 1, tagNameSet)))
                                    ), axis=0)
    return embedding


class PredictServicer(predict_pb2_grpc.PredictionServiceServicer):

    def doPrediction(self, request, context):
        strList = request.s
        return predict_pb2.PredictResponse(probability=predict(strList))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=40))
    predict_pb2_grpc.add_PredictionServiceServicer_to_server(
        PredictServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

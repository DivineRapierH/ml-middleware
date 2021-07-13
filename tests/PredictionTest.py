import unittest

import grpc
import numpy as np

from rpc import predict_pb2_grpc, predict_pb2
from rpc.PredictServer import calcEmbedding


class MyTestCase(unittest.TestCase):
    def calcEmbeddingTest(self):
        sourceStrList = ['月亮与六便士',
                         '(英)毛姆|徐淳刚',
                         '《月亮和六便士》是英国小说家威廉· 萨默赛特·毛姆的三大长篇力作之一，成书于1919年。在这部小说里，毛姆用第一人称的叙述手法，叙述了整个故事。本书情节取材于法国后印象派画家高更的生平，主人公原本是位证券经纪人，中年时舍弃一切到南太平洋的塔希提岛与土著人一起生活，获得灵感，创作出许多艺术杰作。小说所揭示的逃避现实的主题，与西方许多人的追求相吻合，成为20世纪的流行小说。',
                         '长篇小说']
        result = calcEmbedding(sourceStrList)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(128, result.size)

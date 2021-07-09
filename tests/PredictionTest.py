import unittest

from rpc.PredictServer import predict


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sourceStrList = ['月亮与六便士',
                         '(英)毛姆|徐淳刚',
                         '《月亮和六便士》是英国小说家威廉· 萨默赛特·毛姆的三大长篇力作之一，成书于1919年。在这部小说里，毛姆用第一人称的叙述手法，叙述了整个故事。本书情节取材于法国后印象派画家高更的生平，主人公原本是位证券经纪人，中年时舍弃一切到南太平洋的塔希提岛与土著人一起生活，获得灵感，创作出许多艺术杰作。小说所揭示的逃避现实的主题，与西方许多人的追求相吻合，成为20世纪的流行小说。',
                         '长篇小说']
        result = predict(sourceStrList)
        # self.assertIsInstance(result, float)
        # self.assertLessEqual(result, 1.0)
        # self.assertGreaterEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()

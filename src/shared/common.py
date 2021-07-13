import fasttext

from config import MODELS_DIR

ft = fasttext.load_model(MODELS_DIR + '/fasttext/cc.zh.128.bin')

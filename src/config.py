import logging
from os import environ

# Fetch user environment variables
PROJECT_NAME = 'ml-middleware'
PROJECT_VERSION = '0.1.0'
EMBEDDING_VERSION: str = environ.get('MOD_TAGGING_EMBEDDING_VERSION', default='v1')
TF_RPC_SERVER: str = environ.get('MOD_TAGGING_TF_RPC_SERVER', default='localhost:8500')

# Fetch project directory (defined in .Dockerfile)
PROJECT_DIR: str = environ.get('PROJECT_DIR', default='/home/ml-middleware')

# Models directory
MODELS_DIR: str = environ.get('MODELS_DIR', default='/home/models')

import pickle
# import numpy as np
# import tensorflow as tf
import warnings
import os

warnings.filterwarnings('ignore')

# Path to ml_model folder
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ML_PATH = os.path.join(BASE, 'ml_model')

with open(os.path.join(ML_PATH, 'nn_model.pkl'), 'rb') as f:
    load_model = pickle.load(f)
with open(os.path.join(ML_PATH, 'tfidf_vectorizer.pkl'), 'rb') as f:
    tfidf = pickle.load(f)
with open(os.path.join(ML_PATH, 'label_encoder.pkl'), 'rb') as f:
    label_encoder = pickle.load(f)
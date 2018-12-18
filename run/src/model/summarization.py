from __future__ import print_function

import pandas as pd
import keras
import os
os.environ['KERAS_BACKEND'] = 'tensorflow'
from src.model.keras_text_summarization.library.rnn import RecursiveRNN1
import numpy as np


def summarization(string):
    keras.backend.clear_session()
    # np.random.seed(42)
    # data_dir_path = './data'
    model_dir_path = '/Users/kkim2250/Desktop/Project_TextSum/run/src/model'

    # print('loading csv file ...')
    # df = pd.read_csv(data_dir_path + "/fake_or_real_news.csv")
    # df = df.loc[df.index < 1000]
    # X = df['text']
    # Y = df.title

    config = np.load(RecursiveRNN1.get_config_file_path(model_dir_path=model_dir_path)).item()

    summarizer = RecursiveRNN1(config)
    summarizer.load_weights(weight_file_path=RecursiveRNN1.get_weight_file_path(model_dir_path=model_dir_path))

    # print('start predicting ...')
    # for i in np.random.permutation(np.arange(len(X)))[0:20]:
    #     x = X[i]
    #     actual_headline = Y[i]
    headline = summarizer.summarize(string)
        # print('Article: ', x)
        # print('Generated Headline: ', headline)
        # print('Original Headline: ', actual_headline)
    return headline
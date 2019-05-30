import pandas as pd
import codecs
import gc
import time
from gensim.models import Word2Vec
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-qp", "--query_path",
                    help="the path of query corpus", type=str)
parser.add_argument("-tp", "--title_path",
                    help="the path of title corpus", type=str)
parser.add_argument("-f", "--save_folder",
                    help="the folder path of saving vectors", type=str)
args = parser.parse_args()


paths = [args.query_path, args.title_path]
sizes = [10]


# TRAIN_PATH = '/home/kesci/input/bytedance/first-round/train.csv'
# CORPUS_PATH = '/home/kesci/work/corpus/'
QUERY_CORPUS_PATH = args.query_path
TITLE_CORPUS_PATH = args.title_path
SAVE_PATH = args.save_folder

for path in paths:
    f = codecs.open(path, 'r')
    corpus = f.readlines()
    num = len(corpus)
    for i in range(num):
        corpus[i] = corpus[i].split()
    f.close()

    start = time.time()
    print('lauch the Word2Vec trainning process')
    model = Word2Vec(corpus, size=sizes[0], window=3, min_count=1, workers=4)
    model.wv.save_word2vec_format(
        os.path.join(SAVE_PATH,path.split('/')[-1].split('.')[0]+'.bin'), binary=True)
    del corpus
    del model
    gc.collect()
    end = time.time()
    duration = end - start
    print('Word2Vec trainning and model saving cost {:.2f} seconds'.format(
        duration))

# f = codecs.open(TITLE_CORPUS_PATH.format(index), 'r')
# corpus = f.readlines()
# num = len(corpus)
# for i in range(num):
#     corpus[i] = corpus[i].split()
# f.close()
# # os.makedirs('./vectors', exist_ok= True)

# start = time.time()
# print('lauch the Word2Vec trainning process of title')
# model = Word2Vec(corpus, size=100, window=3, min_count=1, workers=4)
# model.wv.save_word2vec_format(
#     '/home/kesci/work/vectors/title_{}.bin'.format(index), binary=True)
# del corpus
# del model
# gc.collect()
# end = time.time()
# duration = end - start
# print('Title Word2Vec trainning and model saving cost {:.2f} seconds'.format(
#     duration))

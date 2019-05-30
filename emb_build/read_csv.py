import argparse
import csv
import codecs
import pandas as pd
import gc
parser = argparse.ArgumentParser()
parser.add_argument("-p1", "--train_path",
                    help="the path of train csv", type=str)
parser.add_argument("-p2", "--test_path",
                    help="the path of test csv", type=str)
# parser.add_argument("-start", "--start_row",
#                     help="the start row of training data", type=int, default=0)
# parser.add_argument("-end", "--end_row",
#                     help="the start row of training data", type=int, default=20000)
# parser.add_argument("-testable", "--read_test",
#                     help="whether to embedded with test file or not", type=bool, default=False)
parser.add_argument("-ap", "--article_path",
                    help="the path of article corpus", type=str)
parser.add_argument("-wp", "--word_seg_path",
                    help="the path of word_seg corpus", type=str)
args = parser.parse_args()
# print(args)
print('loading datasets......')
train_data = pd.read_csv(args.train_path)
print('{} lines in test datasets'.format(len(train_data)))

test_data = pd.read_csv(args.test_path)
print('{} lines in test datasets'.format(len(test_data)))

# print(train_data.head())
print('making article.txt......')
with open(args.article_path, 'w') as f:
    f.writelines([text + '\n' for text in train_data['article']])
    f.writelines([text + '\n' for text in test_data['article']])

print('making word_seg.txt......')
with open(args.word_seg_path, 'w') as f:
    f.writelines([text + '\n' for text in train_data['word_seg']])
    f.writelines([text + '\n' for text in test_data['word_seg']])

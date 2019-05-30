import os
BASE_PATH = os.path.abspath(os.path.curdir)
# 在work中新建embed_build文件
os.makedirs(os.path.join(BASE_PATH,'emb_build'), exist_ok= True)
os.makedirs(os.path.join(BASE_PATH,'emb_build/vectors'), exist_ok= True)
TRAIN_PATH = os.path.join(BASE_PATH, 'data/train_set.csv')
TEST_PATH = os.path.join(BASE_PATH, 'data/test_set.csv')
VEC_SAVE_FOLDER = os.path.join(BASE_PATH,'emb_build/vectors')
ARTICLE_PATH = os.path.join(BASE_PATH, 'emb_build/article.txt')
WORD_SEG_PATH = os.path.join(BASE_PATH, 'emb_build/word_seg.txt')
os.system('python emb_build/read_csv.py -p1 {} -p2 {} -ap {} -wp {}'.format(TRAIN_PATH, TEST_PATH,ARTICLE_PATH, WORD_SEG_PATH))
# os.system('python emb_build/train_emd.py  -qp {} -tp {} -f {}'.format(QUERY_PATH, TITLE_PATH, VEC_SAVE_FOLDER))
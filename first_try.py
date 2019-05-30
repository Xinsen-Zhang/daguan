import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

df_train = pd.read_csv('./train_set.csv')
df_test = pd.read_csv('./test_set.csv')
df_train.drop(columns=['article', 'id'], inplace= True)
df_test.drop(columns=['article'], inplace= True)

vectorizer = CountVectorizer(ngram_range=(1,2), min_df= 3, max_df= 0.9, max_features= 100000)
vectorizer.fit(df_train['word_seg'])
x_train = vectorizer.transform(df_train['word_seg'])
x_etst = vectorizer.transform(df_test['word_seg'])
y_train = df_train['class']-1
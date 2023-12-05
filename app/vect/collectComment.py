import pyprind
import os
import pandas as pd
import numpy as np

pbar = pyprind.ProgBar(50000)
labels = {'pos':1, 'neg':0}
df = pd.DataFrame()
for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        path = 'C:/_Code/Flask/NIR/app/vect/BookRatio/%s/%s' % (s, l)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding = 'utf-8') as infile:
                txt = infile.read()
            df = df._append([[txt, labels[l]]], ignore_index=True)
            pbar.update()
df.columns = ['review', 'sentiment']

# перемешаем DataFrame
np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))   
df.to_csv('C:/_Code/Flask/NIR/app/vect/book_data.csv')

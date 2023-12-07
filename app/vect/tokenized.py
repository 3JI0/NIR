'''Функция лексимизации, которая очищает необработанные текстовые данные из файла, 
    и разделяет их на словарные лексемы , удаляя стоп-слова'''
import numpy as np
import re   
from nltk.corpus import stopwords

stop = stopwords.words('english')
def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W] + ','', text.lower()) + \
    ' '.join(emoticons).replace('-','') 
    tokenized = [w for w in text.split () if w not in stop]
    return tokenized
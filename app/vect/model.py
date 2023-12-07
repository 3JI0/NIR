import pyprind
import numpy as np
from get_minibatch import get_minibatch
from stream_docs import  stream_docs
from hash_vect import vect, clf

pbar = pyprind.ProgBar(45)
classes = np.array([0,1])
doc_stream = stream_docs('C:/_Code/Flask/NIR/app/vect/book_data.csv')
for _ in range(45):
    X_train, y_train = get_minibatch(doc_stream, size = 1000)
    if not X_train:
        break
    X_train = vect.transform(X_train)
    clf.partial_fit(X_train, y_train, classes = classes)
    pbar.update()

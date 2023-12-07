import pickle
import os
from tokenized import stop
from model import clf

dest = os.path.join('bookclassifier','pkl_objects')
if not os.path.exists(dest):
    os.makedirs(dest)
pickle.dump(stop, 
            open(os.path.join(dest, 'stopword.pkl'), 'wb'),
           protocol = 4)
pickle.dump(clf, 
            open(os.path.join(dest, 'classifier.pkl'), 'wb'),
           protocol=4)
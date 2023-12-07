from tokenized import tokenizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier


vect = HashingVectorizer(decode_error='ignore',
                        n_features = 2**21,
                        preprocessor=None,
                        tokenizer=tokenizer)
clf = SGDClassifier(loss='log_loss', random_state=1, max_iter = 1)



#%%
import sys

import numpy as np
from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential
from keras.utils import np_utils
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

corpus = open("corpus.txt").read()
#%%

def tokenize_words(input):
    # lowercase everything to standardize it
    input = input.lower()

    # init tokenizer
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(input)

    # remove stop words as they provide no value in the model
    filtered = filter(lambda token: token not in stopwords.words("english"), tokens)
    return " ".join(filtered)


processed_corpus =  tokenize_words(corpus)

chars = sorted(list(set(processed_corpus)))
char_to_num = {c: i for i, c in enumerate(chars)}

input_len = len(processed_corpus)
vocab_len = len(chars)
print ("Total number of characters:", input_len)
print ("Total vocab:", vocab_len)

# %%

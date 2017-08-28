# need to create a 'hot' array of words
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import pickle
from collections import Counter

lemmatizer = WordNetLemmatizer()
# max number of lines in the dataset
hm_lines = 10000000

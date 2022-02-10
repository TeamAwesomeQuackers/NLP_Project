import pandas as pd
import numpy as np

# Scraping
import requests
from bs4 import BeautifulSoup

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import nltk.sentiment

from wordcloud import WordCloud
# pd.set_option('display.max_colwidth', -1)

# Regex
import re

# Time
from time import strftime

import unicodedata
import json
from pprint import pprint

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Custom Imports
# import acquire 
import prepare
import wrangle

# Turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")


from sklearn.linear_model import LogisticRegression



def print_lr_tfidf_model_train(train):
    from sklearn.metrics import classification_report, accuracy_score
    print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.lr_predicted_tdidf)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(train.lr_predicted_tdidf, train.actual))
    print('---')
    print(classification_report(train.actual, train.lr_predicted_tdidf))

def print_lr_tfidf_model_validate(validate):
    from sklearn.metrics import classification_report, accuracy_score
    print('Accuracy: {:.2%}'.format(accuracy_score(validate.actual, validate.lr_predicted_tdidf)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(validate.lr_predicted_tdidf, validate.actual))
    print('---')
    print(classification_report(validate.actual, validate.lr_predicted_tdidf))


def print_lr_bagofwords_model_train(train):
    from sklearn.metrics import classification_report, accuracy_score
    print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.lr_predicted_bagofwords)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(train.lr_predicted_bagofwords, train.actual))
    print('---')
    print(classification_report(train.actual, train.lr_predicted_bagofwords))


def print_lr_bagofwords_model_validate(validate):
    from sklearn.metrics import classification_report, accuracy_score
    print('Accuracy: {:.2%}'.format(accuracy_score(validate.actual, validate.lr_predicted_bagofwords)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(validate.lr_predicted_bagofwords, validate.actual))
    print('---')
    print(classification_report(validate.actual, validate.lr_predicted_bagofwords))
#!/usr/bin/env python
# coding: utf-8

# ## Notebook Containing all the Prepare Functions for the NLP Project

# ### imports

import pandas as pd

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

from time import strftime

# Custom Imports
# commenting out acquire for the time being, since the runtime is long to import it and there is a json to work from
# import acquire 


def basic_clean(string):
    '''
    This function:
    takes in a string,
    returns the string normalized
    '''
    string = unicodedata.normalize('NFKD', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string


def tokenize(string):
    '''
    This function:
    takes in a string,
    returns a tokenized string
    '''
    # Create tokenizer.
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # Use tokenizer
    string = tokenizer.tokenize(string, return_str = True)
    
    return string


def stem(string):
    '''
    This function:
    takes in a string,
    returns a string with words stemmed
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string


def lemmatize(string):
    '''
    This function:
    takes in string,
    returns a string with words lemmatized
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string


def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function:
    takes in a string, 
    takes in optional extra_words and exclude_words parameters with default empty lists,
    returns a string
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))

    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

def prep_readme_data(df, column, extra_words=[], exclude_words=[]):
    '''
    This function:
    takes in a df and the string name for a text column, 
    takes in option to pass lists for extra_words and exclude_words,
    cleans, tokenizes, and lemmatizes text with stopwords removed,
    returns a df with the readme contents, clean readme contents, stemmed readme contents,
    lemmatized readme contents
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['stemmed'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(stem)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['lemmatized'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(lemmatize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    return df[['readme_contents', column,'clean', 'stemmed', 'lemmatized']]



# to run:
# prep_readme_data(df, 'readme_contents', extra_words = [''], exclude_words = ['']).head()





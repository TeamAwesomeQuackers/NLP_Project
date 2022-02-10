import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
from bs4 import BeautifulSoup
import time
from env import github_token, github_username
import pandas as pd
import numpy as np
import prepare

def common_language(string):
    """
    Takes in a string and compares it to a predefined user list
    if string not in list changes to 'Other'
    """
    language_list= ['JavaScript', 'Python', 'C++', 'PHP', 'C']
    if string not in language_list:
        string = 'Other'
    return string

   # Save the names of the top 5 programming languages, and change the rest to 'Other'
    df['language'] = df.language.apply(common_language)


def split_repos(df):
    from sklearn.model_selection import train_test_split
    # SPLIT
    # Test set is .2 of original dataframe  
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify= df.language)
    # The remainder is here divided .7 to train and .3 to validate
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify= train.language)
    # further splitting into X_ and y_ splits
    X_train = train.drop(columns=['language'])
    y_train = pd.DataFrame(train.language, columns=['language'])

    X_validate = validate.drop(columns=['language'])
    y_validate = pd.DataFrame(validate.language, columns=['language'])

    X_test = test.drop(columns=['language'])
    y_test = pd.DataFrame(test.language, columns=['language'])

    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test



def brian_quick_clean(df):
    df = df.drop_duplicates()
    df = prepare.prep_readme_data(df, 'readme_contents', extra_words=[], exclude_words=[])
    df=df.drop(columns=['readme_contents', 'clean', 'stemmed'])
    df['language'] = df.language.apply(common_language)
    return df


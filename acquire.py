"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
from bs4 import BeautifulSoup
import time
from env import github_token, github_username
import pandas as pd
import numpy as np

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.


    
    
def get_extensions():
    extension_list = []
    for i in range(1,10):
        response = requests.get('https://github.com/search?p='+str(i)+'&q=bitcoin&type=Repositories', headers={'user-agent': 'DS Student'})
        soup = BeautifulSoup(response.text)
        repos = soup.find_all('div', class_ = 'f4 text-normal')
        for repo in repos:
            time.sleep(.000001)
            extension = repo.a.attrs['href']
            extension_list.append(extension)
    extension_list = [n[1:] for n in extension_list]
    return extension_list


REPOS = get_extensions()


headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)

def make_json(cached=False):
    '''
    Function that extracts the title, date_published, and content of every blog post on the Codeup
    blot webpage and returns them in a pandas DataFrame
    '''
    # define a file that the function can look for in case of caching
    filename = 'repo_readmes.json'
    # if a cached json of this name exists, the function reads it directly
    # (unless the caching argument is turned to false)
    if cached==True:
        # checking to see that a cached file actually exists in the directory
        if os.path.isfile(filename):
            # directly read and return the json if it exists
            return pd.read_json(filename)    
        # if cached is set to true, but no file exists in the directory, return a print statement
        # to the effect, and halt the function
        else:
            return print("No cached file exists in this directory, change the 'cached' argument")
    # if the file does not exist or caching is defined as 'False', build the dataframe from 
    # web scraping of the webpage
    else:
        df = pd.DataFrame(scrape_github_data(),columns=['repo','language','readme_contents'])
        # write the resulting DF to json format
        df.to_json('repo_readmes.json')
    return df
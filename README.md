<div align="center">

<img src="Images/github_logo.png" alt="Codeup Logo" title="Codeup Logo" width="225" height="225" align="center"/>      

# README

### by Chloe Whitaker, Jeanette Schulz, Brian Clements, and Paige Guajardo 
### 11 February 2022


</div align="center">
    
<hr style="border:2px solid blue"> </hr>

# About this Project
### Github Webscraping and Natural Language Processing
Millions of developers and companies build, ship, and maintain their software on GitHub— the largest and most advanced development platform in the world. As Codeup's new up-and-coming Data Scientists, we will be using GitHub's platform to practice both our Web-Scraping skills and our Natural Language Processing (NLP) skills. With a focus on repositories that are studying bitcoin, our goal is to predict the programming language used in a repository based solely on the README.md file provided. By exploring the text provided in the README, we hope to identify key words that will allow us to identify which programming language(s) were used. Then we will teach these to our classification model so that it will predict the programming language of any future repositories we show it. The list of languages we will try to predict are:  

- JavaScript  
- Python   
- C++  
- PHP  
- C  
- Java  
- Other  

<hr style="border:2px solid blue"> </hr>

# Project Planning
## Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

<b>Planning:</b>  
- Make sure we have access to GitHub webscraping (GitHub prefers the use of thier API)
- Create a repository to save all our work

<b>Acquisition </b>  
- Collect the data through webscraping GitHub's API 
- Create an `acquire.py` file to make future acquisition easier

<b>Preparation</b>  
- Clean the acquired data
  - Remove special characters
  - Tokenize and Lemmatize the words of each corpus
  - Drop a very few duplicates and nulls that existed
  - Redefine any language that had few observations as "other"
- Create a `prepare.py` file to make future data cleaning easier
- Organize our repository for easy navigation
  - Images directory to hold all photos used
  - Workbook directory to hold all work done
  - Write a README file

<b>Exploration and Pre-processing</b>  
- Explore data to find key words used in the README files 
- Summarize takeaways and conclusions

<b>Modeling</b>  
- Create a Classification model that will predict the programming language used in a repository, based on the repositories README text.

<b>Deliver</b>  
- A `Final_Report.ipynb` to explain our findings and results.
- A 5 minute presentation via Google slides 

<hr style="border:2px solid blue"> </hr>

# Data Dictionary

| Feature                    | Datatype               | Description                                                           |
|:---------------------------|:-----------------------|:----------------------------------------------------------------------|
| repo                       | 166 non-null: object   | github repo name             |
| language                   | 166 non-null: object   | repo programming language            |
| readme_contents            | 166 non-null: object   | contents of the repo's readme             |

Many variables were also defined:
Splits, along the lines of TRAIN, VALIDATE, TEST, X_splits, and y_splits for each
JavaScript_words (etc. according to language) : the words of all corpii that belong to that language
JavaScript_freq (etc. according to language) : the frequency of any given word, by language used to build the following
word_counts: dataframe that reports the number of occurences of any given lemmatized word, across all languages
length_list: a list of the lengths of all words belonging to any given language

<hr style="border:2px solid blue"> </hr>

# Steps to Reproduce

To run the `Final_NLP_Project.ipynb` notebook on your own computer you will need to:

 1. Read this README.md (check!)
 2. Download the whole repository 
 3. Create your own env.py file and add the following
 4. Make a github personal access token.
    - Go here and generate a personal access token https://github.com/settings/tokens 
          - You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
    - Save it in your env.py file under the variable `github_token`
    - Add your github username to your env.py file under the variable `github_username`

 5. Copy your env.py file into the NLP_Project directory 
 6. Run the `Final_NLP_Project.ipynb` in a jupyter notebook

<hr style="border:2px solid blue"> </hr>

# Initial Hypothesis

Our intial thought is that a lot of the READMEs contain unique words that could help predict the language of the repository. 

# Some Questions We Hope to Answer for this Project:

1. What are the most frequently occuring words in the readmes?
2. Are there words that uniquely identify with a certain language's repos?
3. What are the least frequently occuring words in the readmes?
4. Does the length of the README vary by programming language?
5. How many repos have their programming language mentioned in the README text?

<div align="center">

<img src="Images/github_logo.png" alt="Codeup Logo" title="Codeup Logo" width="225" height="225" align="center"/>      

# README

### by Chloe Whitaker, Jeanette Schulz, Brian Clements, and Paige Guajardo 
### 11 February 2022


</div align="center">
    
<hr style="border:2px solid blue"> </hr>

# About this Project
### Github Webscraping and Natural Language Processing
Millions of developers and companies build, ship, and maintain their software on GitHub— the largest and most advanced development platform in the world. As Codeup's new up-and-coming Data Scientists, we will be using GitHub's platform to practice both our Web-Scraping skills and our Natural Language Processing (NLP) skills. With a focus on repositories that are studying bitcoin, our goal is to predict the programming language used in a repository based solely on the README.md file provided. By exploring the text provided in the README, we hope to identify key words that will allow us to identify which programming language(s) were used. Then we will teach these to our classification model so that it will predict the programming language of any future repositories we show it. For now, the list of languages whose detection is supported is as follows:
    - JavaScript
    - Python
    - Go
    - C++
    - Java
    - TypeScript
    - HTML
    - PHP
    - C#


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
| feature_name                       | 847330 non-null: object  | feature described here             |
| feature_name                       | 847330 non-null: object  | feature described here             |
| feature_name                       | 847330 non-null: object  | feature described here             |
| feature_name                       | 847330 non-null: object  | feature described here             |
| feature_name                       | 847330 non-null: object  | feature described here             |

<hr style="border:2px solid blue"> </hr>

# Steps to Reproduce

To run the `Final_Report.ipynb` notebook on your own computer you will need to:

 1. Read this README.md (check!)
 3. Download the whole repository 
 4. Copy your own env.py file into the repository 
 8. Run the `Final_Report.ipynb` in a jupyter notebook

<hr style="border:2px solid blue"> </hr>


# Questions we hope to answer for this Project:

1. What are the most common words in READMEs?
2. What does the distribution of IDF's look like for the most common words?
3. Does the length of the README vary by programming language?
4. Do different programming languages use a different number of unique words?

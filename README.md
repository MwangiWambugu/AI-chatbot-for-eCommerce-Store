# AI-chatbot-for-eCommerce-Store
![Alt text](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/blob/main/images/best-ai-chatbot-software.png)

## Problem Statement
To develop an AI-powered chatbot designed to provide responsive, context-aware assistance without the limitations of human-operated systems

## Project Overview
The Chatbot was developed by utilizing Natural Language Processing (NLP) techniques to enhance customer interactions and provide personalized assistance.

## Business Understanding
In the dynamic realm of artificial intelligence, the utilization of AI chatbots has become increasingly integral, presenting numerous opportunities for transformative applications. This project focuses on the development of versatile AI chatbots designed to serve as customer support. Leveraging advanced natural language processing and machine learning techniques, the goal is to craft intelligent conversational agents capable of elevating user experiences across a spectrum of domains.


## Components

* **Jupyter Notebook**
The [Jupyter Notebook](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store) Our key deliverable contains details of our approach and methodology, data cleaning, exploratory data analysis, and model building, validation and deployment.

I recommend using [nbviewer](https://nbviewer.jupyter.org/) to view the Jupyter Notebook.

* **Presentation**
The [presentation](https://) gives a high-level overview of our approach, findings and recommendations for non-technical stakeholders. It is aimed to be between 5 and 10 minutes long.

* **Data**

The dataset can be found in the file *"QA_Beauty.json.gz"* in this repository. It was originally provided in the following [repository](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store).

## Technologies/ Packages

* Python version: 3.11.9
* Matplotlib version: 3.1.3
* Seaborn version: 0.9.0
* Pandas version: 0.25.1
* Numpy version: 1.16.5
* Statsmodels version: 0.10.1
* Scikit-learn version: 0.21.2 
* TensorFlow version: v2.15.0
* statistics version: 3.2
* nltk version: 3.10


## To get started

1. Clone this repository - [guidance](https://help.github.com/articles/cloning-a-repository/).
2. Dataset can be found in the file "QA_Beauty.json.gz".
3. Check the requirements in the Technologies section above and download libraries if necessary.

## 1. Data Wrangling
Here we will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping, and other processes to ensure that we have a clean, structured, and suitable format for analysis and modeling

## 2. Exploratory Data Analysis (EDA)
The graph presented is a univariate bar plot that displays the distribution of question types within a dataset. This dataset appears to be related to an e-commerce setting question/answer data.
Open-ended: This category has the largest number of occurrences, indicating that it is the most common type of question in the dataset.
Yes/no: This category has a much lower count in comparison to open-ended questions, indicating that such questions are less frequent in the dataset.
![image](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/blob/main/images/univariate%20analysis.png)

The histogram shows that the majority of questions receive a specific number of answers, with the number two being the most common, as indicated by the highest bar on the graph.
![image](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/blob/main/images/distribution.png)

The visualization displays the top 20 most frequently occurring words found in questions from the dataset. These types of words are typically used in text analysis to understand the common language or topics that are being discussed.
![image](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/blob/main/images/most_common_words_bar_chart.png)

In this word cloud, we can identify several prominent words: "product", "use", "work", "will", "thanks" and "one"
![image](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/blob/main/images/wordcloud.png)

"is this" is the most frequent bi-gram, suggesting that many questions start with an inquiry directly about a product or feature.
"what is the" is the most frequent tri-gram, which is often a lead into a detailed question about a product or service.
![image](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/blob/main/images/most_common_ngrams_subplot.png) 

## 3. Data Preprocessing
Parsing and analyzing data from  the compressed JSON file containing beauty-related questions and answers, extracting relevant columns such as question type, question text, and top answers, and then displaying them.
Aggregating questions and answers into a structured format and writes them to a JSON file for further processing.

#### 3.1 Tokenizing
A function that pairs questions with their corresponding responses from a list of dictionaries, assuming each sublist contains dictionaries with `'tag'`, `'questions'`, and `'responses'` keys, and returns a list of dictionaries with `'tag'`, `'question'`, and `'response'` keys.

#### 3.2 Lemmatizing Words using NLTK
Lemmatize words in a list of filtered words, and then prints a sample of the lemmatized words.


## 4. Modelling
#### Multinomial Naive Bayes Model


## 5. Conclusion

## Contributors:
|Name     |  GitHub   |
|---------|-----------------|
|Mwangi Wambugu |https://github.com/MwangiWambugu|
|Paul Kamau |https://github.com/KPaul404|
|Mercy Tegekson |https://github.com/mercytegekson|
|Laureen Chepkoech |https://github.com/Lawrync|
|Stephen Butiya |https://github.com/obystephen|
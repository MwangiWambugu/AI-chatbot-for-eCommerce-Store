# AI-chatbot-for-eCommerce-Store

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
2. Dataset can be found in the file "zillow_data.csv".
3. Check the requirements in the Technologies section above and download libraries if necessary.

## 1. Data Wrangling
Here we will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping, and other processes to ensure that we have a clean, structured, and suitable format for analysis and modeling

## 2. Exploratory Data Analysis (EDA)
![image](https://github.com/MwangiWambugu/AI-chatbot-for-eCommerce-Store/tree/stephen)


## 3. Data Preprocessing
Parsing and analyzing data from  the compressed JSON file containing beauty-related questions and answers, extracting relevant columns such as question type, question text, and top answers, and then displaying them.
Aggregating questions and answers into a structured format and writes them to a JSON file for further processing.

# 3.1 Tokenizing
A function that pairs questions with their corresponding responses from a list of dictionaries, assuming each sublist contains dictionaries with `'tag'`, `'questions'`, and `'responses'` keys, and returns a list of dictionaries with `'tag'`, `'question'`, and `'response'` keys.

# 3.2 Lemmatizing Words using NLTK
Lemmatize words in a list of filtered words, and then prints a sample of the lemmatized words.


## 4. Modelling


## Multinomial Naive Bayes Model
Accuracy: 0.06140983486328244
Classification Report:
                                precision    recall  f1-score   support

  Accessories and Attachments       0.05      0.05      0.05      6704
                  Electronics       0.05      0.04      0.04      6723
                    Fragrance       0.04      0.03      0.04      6485
            Health and Safety       0.02      0.01      0.02      6603
Ingredient Specific Questions       0.03      0.02      0.03      6664
       International Shipping       0.03      0.02      0.03      6671
                Personal Care       0.12      0.20      0.15      7604
         Product Authenticity       0.05      0.03      0.04      6778
           Product Comparison       0.07      0.06      0.06      6735
       Shipping and Packaging       0.07      0.07      0.07      6804
           Usage Instructions       0.10      0.10      0.10      7393
Warranty and Customer Support       0.04      0.06      0.05      6647

                     accuracy                           0.06     81811
                    macro avg       0.05      0.06      0.06     81811
                 weighted avg       0.06      0.06      0.06     81811

Accuracy on the test set: 0.06
Cross-Validation Scores: [0.07182396 0.07228982 0.07205689 0.0704812  0.07178286]
Mean Accuracy: 0.07168694508385401

## Contributors:
|Name     |  GitHub   |
|---------|-----------------|
|Mwangi Wambugu |https://github.com/MwangiWambugu|
|Paul Kamau |https://github.com/KPaul404|
|Mercy Tegekson |https://github.com/mercytegekson|
|Laureen Chepkoech |https://github.com/Lawrync|
|Stephen Butiya |https://github.com/obystephen|
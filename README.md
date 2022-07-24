![image](https://user-images.githubusercontent.com/99698846/178391954-a755f5b3-798b-4f94-adf1-33a98af93948.png)

# fake_news

## Overview
Group 3 selected “fake news” for the final project. The intent of the analysis is to identify fake news articles based on the title, author, and text within the article. The dataset categorizes each article with a 0 or 1 — the 0 is indicative of a reliable source (therefore not fake news) and a 1 is indicative of fake news!  
Long short-term memory (LSTM) was utilized to conduct this analysis. 

## Presentation
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRmQPvgaKRaGcQUUh_QWeqbyAoyczvgGxaKWcnog9yyZ4bgXTVx8T_yNyqK57dqL12awufPEvM0loBH/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Fake News—why?
Identifying reputable sources for news has become a necessity considering the political climate It is crucial for individuals to access accurate and truthful information in order to make decisions based on facts

## Data Source
fake_news dataset was found on Kaggle as part of a large community that has implemented big machine learning models and deep learning under this dataset.
In this project, the main two datas that we are using are test and train table and it is located in the Data folder.
The Links to the original data sets are below:

1) [Test](https://www.kaggle.com/code/duquochuy/fake-news-detection-using-lstm-90-accuracy/data?select=test.csv)

2) [Train](https://www.kaggle.com/code/duquochuy/fake-news-detection-using-lstm-90-accuracy/data?select=train.csv)

### Description of tools used:
1) Jupyter Notebook
2) PostgreSQL
3) pgAdmin
4) GitHub
5) Google Slides

## Cleaned Data Source
Our team used Pandas'library to read, clean the data. 
### Fake_test_data 
![fake_test_data](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_test_data.PNG)
### Fake_new_df
![fake_news_data](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news_df.PNG)

### Fake_news_final
Then, we drop Rows with Missing Values in any row. The dataset became 18285 rows * 5 columns. After that, we merged fake_test_clean and fake_new_clean 
![fake_news_final](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news_final.png)
PICTURE 

## ETL Jupyter Notebook & pg_Admin

The process we used for our database was the following: 
1.
2.
3.

 we used the clean table in jupyter notebook to link onto out local database through pgAdmin.

![Joined table](https://github.com/cindyhdz/fake_news/blob/main/Resources/SQL%20Joined%20Table.png)

## Machine Learning 
1) Logistic regression predicts binary outcomes, indicative of only two possible outcomes. The model determines the probability by analyzing the available data, presented with a new sample. If the probability is above a certain limit, the sample is assigned to the class. If it is less than, the sample is assigned to the other class. For this dataset, it examines where news is fake or not.  


![logistic](https://github.com/cindyhdz/fake_news/blob/main/Resources/logistic.png)

2) Random forest model is known as an ensemble classification, which is the process of combining multiple models. It will sample the data and build several smaller, simple decision trees with controlled variation. As a result, it reduces the over-fitting problem while increasing accuracy. For the fake news dataset, random forest classifier will predict if the articles are fake or not too.

![random_forest](https://github.com/cindyhdz/fake_news/blob/main/Resources/random_forest.png)
### Results
![results](https://github.com/cindyhdz/fake_news/blob/main/Resources/results.png)


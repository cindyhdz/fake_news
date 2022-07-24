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

## ETL Jupyter Notebook & pg_Admin

### Cleaned Data Source

1. Using Jupyter Notebook, our team used Pandas'library to read and clean the data:

 - We created dataframes by using from test.csv and train.csv using 'pd.read_csv' as shown below:
   #### Fake_test_df 
   ![fake_test_data](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_test_data.PNG)

    - Drop all null values: 
      ![Drop null 1](https://github.com/cindyhdz/fake_news/blob/main/Resources/dropna%201.png)

   #### Fake_news_df
   ![fake_train_data](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_train%20df.png)

    - Drop all null values: 
      ![Drop null 2](https://github.com/cindyhdz/fake_news/blob/main/Resources/dropna%202.png)

2. To load the data we used PGadmin: 
 
 - Then we created new both tables in PostgresSQL: 
   #### fake_test
   ![fake_test](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_test%20sql.png)

   #### fake_news
   ![fake_news](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news%20sql.png)
   
3. In PGadmin we joined both tables: 

 - Created new table 'joined_df' and deleted null values from columns:
   #### joined_df
   ![Joined table](https://github.com/cindyhdz/fake_news/blob/main/Resources/SQL%20Joined%20Table.png)
   
4. Extract joined_df table to jupyter notebook and update columns:
 - New table as fake_news_clean:
   #### fake_news_clean
   ![fake_news_clean](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news_clean.png)
  
 - New 'merge' column and update columns:
   ![merge_column](https://github.com/cindyhdz/fake_news/blob/main/Resources/merged%20%26%20update%20columns.png)

5. Finish creating final table to PGadmin: 
   #### fake_news_final
   ![final_table](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news_final.png)
 
## Machine Learning 
1) Logistic regression predicts binary outcomes, indicative of only two possible outcomes. The model determines the probability by analyzing the available data, presented with a new sample. If the probability is above a certain limit, the sample is assigned to the class. If it is less than, the sample is assigned to the other class. For this dataset, it examines where news is fake or not.  


![logistic](https://github.com/cindyhdz/fake_news/blob/main/Resources/logistic.png)

2) Random forest model is known as an ensemble classification, which is the process of combining multiple models. It will sample the data and build several smaller, simple decision trees with controlled variation. As a result, it reduces the over-fitting problem while increasing accuracy. For the fake news dataset, random forest classifier will predict if the articles are fake or not too.

![random_forest](https://github.com/cindyhdz/fake_news/blob/main/Resources/random_forest.png)
### Results
![results](https://github.com/cindyhdz/fake_news/blob/main/Resources/results.png)


![image](https://user-images.githubusercontent.com/99698846/178391954-a755f5b3-798b-4f94-adf1-33a98af93948.png)

# fake_news

## Overview:
Group 3 selected “fake news” for the final project. The intent of the analysis is to identify fake news articles based on the title, author, and text within the article. The dataset categorizes each article with a 0 or 1 — the 0 is indicative of a reliable source (therefore not fake news) and a 1 is indicative of fake news!  
Long short-term memory (LSTM) was utilized to conduct this analysis.

## Topic: Predicting fake news

## Presentation:
https://docs.google.com/presentation/d/1HgytebzNI7wfJLkVbW6OMDnbeQiYflKutzJi2lEPdvw/edit#slide=id.g13ff610b84a_0_50

## Fake News—why?
Identifying reputable sources for news has become a necessity considering the political climate It is crucial for individuals to access accurate and truthful information in order to make decisions based on facts

## Data Source:
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

## ETL: Jupyter Notebook & pg_Admin

### Cleaned Data Source:

1. Using Jupyter Notebook, our team used Pandas to read and clean the data:

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
   
### ERD 

![ERD](https://github.com/cindyhdz/fake_news/blob/main/Resources/ERD/fake_news%20ERD.png)

 
## Machine Learning:
The steps start with cleaning data by removing unnecessary special characters, numbers, and white spaces, and finally, removing stop words is implemented. Then, we use one hot method to prepare data before it can be fit to a particular machine learning model. This means we convert the title column from textual data to numerical data. Then, this is where pad sequence is used to add zeros to make the line the same length. After that we start creating our model. We investigated 3 different machine learning which are logistic regression, random forest classifier and Long term short memory(LTSM). 

1) Long term short memory is designed to recognize patterns in sequences of data. It consists of multiple algorithms that is majorly used to analyze the relationship between data points. The first layer is the Embedding layer which will convert the number array which we saw above into a vector of 40 dimensions, and then we have an LSTM layer with 100 nodes. After that we converting X and y to numpy arrays and simply splitting the data using traintestsplit. We assigned the X to input variables, and used them to predict Y, the output. The label column is defined as Y. X is created by dropping the label column from the data frame. This method compares the actual label column from the test against the models’ predicted values.

2) Logistic regression predicts binary outcomes, indicative of only two possible outcomes. The model determines the probability by analyzing the available data, presented with a new sample. If the probability is above a certain limit, the sample is assigned to the class. If it is less than, the sample is assigned to the other class. For this dataset, it examines where news is fake or not.  


![logistic](https://github.com/cindyhdz/fake_news/blob/main/Resources/logistic.png)

3) Random forest model is known as an ensemble classification, which is the process of combining multiple models. It will sample the data and build several smaller, simple decision trees with controlled variation. As a result, it reduces the over-fitting problem while increasing accuracy. For the fake news dataset, random forest classifier will predict if the articles are fake or not too.

![random_forest](https://github.com/cindyhdz/fake_news/blob/main/Resources/random_forest.png)
### Results
In 2022, almost everyone relies on online news. Creating fake news and spreading through social media has become easy for people who wants followers or wants to monetize their content. For that reason, we perform two different  machine learning algorithms and they are random forest and logistic regression. The results shows that random forest has the best accuracy with 0.91 compared to logistic regression that was 0.73.




## Dashboard:

- Tableau: https://public.tableau.com/authoring/Fake_news_16593155646010/Dashboard1#1




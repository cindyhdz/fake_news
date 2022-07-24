![image](https://user-images.githubusercontent.com/99698846/178391954-a755f5b3-798b-4f94-adf1-33a98af93948.png)

# fake_news

## Overview
Group 3 selected “fake news” for the final project. The intent of the analysis is to identify fake news articles based on the title, author, and text within the article. The dataset categorizes each article with a 0 or 1 — the 0 is indicative of a reliable source (therefore not fake news) and a 1 is indicative of fake news!  
Long short-term memory (LSTM) was utilized to conduct this analysis. 

## Fake News—why?
Due to the inclement political climate, identifying reputable sources for news information has become a necessity to make responsible choices at the polls. Additionally, we as a group believe that it's only ethical to supply citizens with accurate and truthful information in order to make decisions based on facts.

## Data Source
fake_news dataset was found on Kaggle as part of a large community that has implemented big machine learning models and deep learning under this dataset.
## Data $ Database
In this project, the main two datas that we are using are test and train
### Description of Datasets
Our main data were found in Kaggle and is located in Data folder.
The Links to the original data sets are below:

1) [Test](https://www.kaggle.com/code/duquochuy/fake-news-detection-using-lstm-90-accuracy/data?select=test.csv)

2) [Train](https://www.kaggle.com/code/duquochuy/fake-news-detection-using-lstm-90-accuracy/data?select=train.csv)
### Entity Relationship Diagram (ERD)

### Cleaned Data Source
Our team used Pandas'library to read, clean the data. 
## Fake_test_data 
![fake_test_data](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_test_data.PNG)
## Fake_new_df
![fake_news_data](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news_df.PNG)

## Fake_news_final
Then, we drop Rows with Missing Values in any row. The dataset became 18285 rows * 5 columns. After that, we merged fake_test_clean and fake_new_clean 
![fake_news_final](https://github.com/cindyhdz/fake_news/blob/main/Resources/fake_news_final.png)
PICTURE 
## ETL pg_Admin
 we used the clean table in jupyter notebook to link onto out local database through pgAdmin.

Picture
## Machine Learning 
1) Logistic Regression predicts binary outcomes, meaning that there are onnly 2 possible outcomes. The model analyzes the available data, and presented with a new sample, matemaytically determine its probability of belonging to a class. If the probablilty is above a certain cutoff point, the sample is assigned to the class. If it is less then the sample is assigened to the other class. In this example, LOGISTIC REGRESSION might decide whether the news are fake or not.

![logistic](https://github.com/cindyhdz/fake_news/blob/main/Resources/logistic.png)

2) Random forest model is known as an ensemble classification which is the process of combining multiple models. It will sample the data and build several smaller, simple decision trees with controlled variation. As a result, it reduces the over-fitting problem while increasing accuracy. In this example Random forest classifier will predict if the articles are faker or not too.

![random_forest](https://github.com/cindyhdz/fake_news/blob/main/Resources/random_forest.png)
### Results
![results](https://github.com/cindyhdz/fake_news/blob/main/Resources/results.png)


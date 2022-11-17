# Disaster Response Pipeline Project

<img width="1198" alt="banner" src="https://user-images.githubusercontent.com/92649864/152714276-607d2d64-c9c9-4aaf-bf87-edea5031d66e.png">


## Project Description
In this project, I will create a machine learning/NLP pipeline to categorize these events and build a model to classify messages that are sent during disasters. There are 36 pre-defined categories, and examples of these categories include Aid Related, Medical Help, Search And Rescue, etc. By classifying these messages, we can allow these messages to be sent to the appropriate disaster relief agency. The dataset -provided by Figure Eight- is used to build a model that classifies disaster messages, while the web app is where a respondent can input a new message and get classification results in several categories.

Finally, this project also contains a web app that allows you to input a message and get classification results.

## File Description
~~~~~
 disaster_response_pipeline
          |-- app
                |-- templates
                        |-- go.html
                        |-- master.html
                |-- run.py
          |-- data
                |-- disaster_message.csv
                |-- disaster_categories.csv
                |-- DisasterResponse.db
                |-- process_data.py
          |-- models
                |-- classifier.pkl
                |-- train_classifier.py
          |-- Preparation
                |-- categories.csv
                |-- ETL Pipeline Preparation.ipynb
                |-- ETL_Preparation.db
                |-- messages.csv
                |-- ML Pipeline Preparation.ipynb
          |-- README
~~~~~
## Installation
Here are the different packages used for this project:

	- Numpy, Pandas, Sklearn
    - NLTK
    - SQLalchemy
    - Flask, Plotly

After you've installed and imported all the necessary packages, you can run the program by following the steps below!

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

#### Notice: You do not to run the Preparation folder to make the program work.

## Screenshots
#### Screenshot 1
<img width="1056" alt="dis  message cate" src="https://user-images.githubusercontent.com/92649864/152714519-127111eb-d2d8-4544-95c1-d713bcef682f.png">

#### Screenshot 2
<img width="1167" alt="dis  message genre" src="https://user-images.githubusercontent.com/92649864/152714578-d7391d45-baac-4563-97cd-6287518d460e.png">

## Licensing, Authors, Acknowledgements
This app was completed as part of the [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

Special thanks to Figure Eight for providing the datasets and giving me the chance to do this project.

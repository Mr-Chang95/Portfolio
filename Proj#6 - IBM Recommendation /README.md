# IBM Recommendation Engine

## Overview
This project was designed to analyze the interactions that users have with articles on the IBM Watson Studio platform, and make recommendations to them about new articles that they might be interested in.

## Packages
List of packages used:
~~~~~
- Matplotlib
- Numpy
- Pandas
- Pickle
~~~~~

## Summary:
The project contains the following tasks:
- Exploratory Data Analysis: This part is for data exploration.

- Rank Based Recommendations: Here, I begin by finding the most popular articles based on the most interactions. These  articles are the ones that we might recommend to new users.

- User-User Based Collaborative Filtering: In order to give better recommendations to the users of IBM's platform, I examine users that are similar in terms of the items they have interacted with. These items could then be recommended to similar users.

- Matrix Factorization: For the final step, I created a machine learning approach to building recommendations. Using the user-item interactions, I built out a matrix decomposition which helps me in predicting new articles an individual might interact with .

## Acknowledgement
I would like to acknowledge and thank [Udacity](https://udacity.com/) for giving me the chance to work on this project. I would also like to thanks [IBM](https://dataplatform.cloud.ibm.com/) for providing the data.

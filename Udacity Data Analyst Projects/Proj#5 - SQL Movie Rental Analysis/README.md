# Investigating Sakila DVD Rental Database
## by Daniel Chang

![movie sql](https://user-images.githubusercontent.com/92649864/160714167-1ed61085-4bf9-4178-9ea7-291ee3943bcb.jpg)

## Summary of Project
In this project, I will be querying the Sakila DVD Rental database which holds information about a company that rents DVDs. I am doing this to gain an understanding gain an understanding of the customer base and to answer the questions listed below:
~~~~~
- Who were the top 10 most-rented actor of 2006?
- How many rentals are missing from each category at the Woodridge store?
- How much did the top 20 districts each spend?
- For the 15 top-spending district, by how much are they outperforming the preceding district?
~~~~~
This project is done as part of the [Udacity Programming for Data Science with Python Nanodegree Program](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104). While the goal os this project is to investigate the database and create visuals answering the questions listed above, this project is also an opportunity to showcase what I've learned as part of the Nanodegree program. Some skills I would like to draw attention to are my ability to join many tables, create window function, create Common Table Expressions(CTE) and perform calculations with the help of logical operators.

The querying phase was performed using [PostgresSQL](https://www.postgresql.org/) and the resulting tables were then saved as .csv files. The visuals were then created using Google Sheets and Slides.

## Installtion
While you can use PostgresSQL to query your the movie rental database, there many other SQL program that you can use instead such as MySQL and Google Big Query. It is completely up to you!

The database used in this project can be found on the PostgresSQL website using the [this link](https://www.postgresqltutorial.com/load-postgresql-sample-database/).

## Files
`movie_insights.sql` : This SQL file is where all the querying happen to gain an understanding and insights from the database, answer the questions asked, and prepare the resulting tables for visualization.
`movie slide and visuals.pdf` : A pdf file with visual slides answering the questions asked.
`dvdrental.tar` : This is the database file where there are 14 tables related to the rental dvds and business.
`dvd-rental-erd.pdf` : A pdf that contains the Entity Relationship Diagram(ERD) of the dvd rental database.

## Licensing, Authors, Acknowledgements
I would like to thank Udacity and PostgresSQL for providing me with the oppurtunity to work on my SQL skills and for the data.

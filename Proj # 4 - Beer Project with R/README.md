# DS 6306 - Beer Project

## Project Description
We want to analyze 2 datasets(totalbeer.csv and totalbreweries.csv) to gain actionable insights to present to the CEO and CFO of Budweiser. Budweiser has hired us to answer some questions. We will perform Exploratory Data Analysis to answer the questions that they are interested in, all of which are listed down below.

The powerpoint was done as a group with my partners: Anthony Burton-Cordova, Yixiao Deng, & Xavier Mojica.

The entire process will be done in R.

## Questions
1. How many breweries are present in each state?
2. Merge beer data with the breweries data. Print the first 6 observations and the last six observations to check the merged file.  (RMD only, this does not need to be included in the presentation or the deck.)
3. Address the missing values in each column.
4. Compute the median alcohol content and international bitterness unit for each state. Plot a bar chart to compare.
5. Which state has the maximum alcoholic (ABV) beer? Which state has the most bitter (IBU) beer?
6. Comment on the summary statistics and distribution of the ABV variable.
7. Is there an apparent relationship between the bitterness of the beer and its alcoholic content? Draw a scatter plot.  Make your best judgment of a relationship and EXPLAIN your answer.
8. Budweiser would also like to investigate the difference with respect to IBU and ABV between IPAs (India Pale Ales) and other types of Ale (any beer with “Ale” in its name other than IPA).  You decide to use KNN classification to investigate this relationship.  Provide statistical evidence one way or the other. You can of course assume your audience is comfortable with percentages … KNN is very easy to understand conceptually.
In addition, while you have decided to use KNN to investigate this relationship (KNN is required) you may also feel free to supplement your response to this question with any other methods or techniques you have learned.  Creativity and alternative solutions are always encouraged.  
9. Find one other useful inference from the data that you feel Budweiser may be able to find value in.  You must convince them why it is important and back up your conviction with appropriate statistical evidence.

## Required Packages
library(dplyr) <br>
library(ggplot2) <br>
library(tidyr) <br>
library(tidyverse) <br>
library(knitr) <br>
library(rmarkdown) <br>
library(caret) <br>
library(class) <br>

# Google Drive presentation
Please visit this [link](https://drive.google.com/file/d/1J7jVk0x34jSrC-mo0A2ze1lgJp6ig-NJ/view?usp=sharing) for my presentation on this project.

## Licensing and Acknowledgements
This was done as a project for Data Science 6306 at Southern Methodist University,

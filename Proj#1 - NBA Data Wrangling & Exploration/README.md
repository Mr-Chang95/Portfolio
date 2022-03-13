# NBA Teams Offensive Data Exploration (1980-2021)
## by Daniel Chang

![Nba](https://user-images.githubusercontent.com/92649864/158081373-686d5f15-09af-407b-be18-cf9ec831f505.png)

## Summary of Project
For this project, I am mainly interested in conducting data exploration and analysis on the offensive stats and characteristics of different NBA teams based on Finals ranking which is a new column I will create that contains 4 values: Champion, Runner-Up, Knocked Out and Never Qualified. Knocked Out and Never Qualified implies that they have either been knocked out of or never qualified for the NBA playoffs. Some stats that you will see me analyze and visualize are Margin of Victory(MOV), 3P%, Age and shot attempts.

`Part I - NBA Web Scraping.ipynb` - To begin, I scraped data from the **[Basketball Reference](https://www.basketball-reference.com/leagues/)**  website, which contains each team's performances throughout the years. I scraped a total of 4 different stats table from the website and stored them in 4 different datasets. In this notebook, I used 3 different packages: Pandas, BeautifulSoup and Requests.

`Part II - NBA Data Cleaning.ipynb` - In this notebook, I conducted the cleaning process. Some steps I took here are dealing with null values, dropping unneeded columns, converting datatypes and cleaning up the values.
After cleaning up the data, I merged 4 of the datasets into 2. I have also created a new column to indicate the NBA teams' Finals ranking in this notebook. One consists of the teams' total stats per year and one consists of the average stats per game of each year. In this notebook, I used 2 different packages: Pandas and Numpy.

`Part III - NBA Data Exploration.ipynb` - For this notebook, you'll find my analysis and visualizations of the stats. I started off by analyzing for the total stats first to get a broad picture view by conducting and creating visuals for univariate and bivariate exploration. Afterward, I moved onto the average stats per game of each year where I conducted the same type of explorations along with multivariate exploration. You will find that I have also created a couple categorical variables for my analysis as well. In this notebook, I used 5 different packages: Pandas, Numpy, Seaborn, Matplotlib and Warnings.

## Installation
~~~~~
* BeautifulSoup
* Requests
* Matplotlib
* Seaborn
* Numpy
* Pandas
* Warnings
~~~~~

## Datasets
 `total_stats_df.csv` - Uncleaned dataset that contains the total stats from 1980-2021 scraped from the Basketball Reference website.

 `avg_stats_df.csv` -  Uncleaned dataset that contains the average stats from 1980-2021 scraped from the Basketball Reference website.

`advanced_stats_df.csv` - Uncleaned dataset that contains the advanced stats from 1980-2021 scraped from the Basketball Reference website. This dataset include variable such as MOV, ORtg and DRtg.

`advanced_stats_df.csv` - Uncleaned dataset that contains the season summary from 1980-2021 scraped from the Basketball Reference website. This dataset include variable such as Champions and Runner-up.

`cleaned_total_stats.csv` - Cleaned dataset that contains the total stats from 1980-2021 scraped from the Basketball Reference website. This dataset all needed variables such as Finals rankings(Finals_Rk).

`cleaned_avg_stats.csv` - Cleaned dataset that contains the average stats from 1980-2021 scraped from the Basketball Reference website. This dataset all needed variables such as Finals rankings(Finals_Rk), Age and Wins.

## Licensing, Authors, Acknowledgements
I would like to give special thanks to **[Basketball Reference](https://www.basketball-reference.com/leagues/)** for the data that I have collected. This couldn't have happened without them.

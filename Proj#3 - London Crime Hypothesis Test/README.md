# London Crime Hypothesis Testing (2008-2016)
## by Daniel Chang

## Summary of Project
In this project, I am interested in working to understand the crime rate in London, England. My goal is to work through this notebook to understand violent crime rates and when they are likely to occur throughout the year. This dataset contains all crimes (non-violent and violent) committed between 2008 and 2016. However, the nature of the crime-violent or non-violent- is not specified in this dataset, so we will need to deal with that during the preprocessing phase. We will also need to specify which months are the ones when daylight saving is in effect.

There are a total of 2 notebooks dedicated to this project. This first notebook(London Crime Hypothesis Testing.ipynb) is dedicated to testing the individual factors(borough/location & daylight saving) that I think may affect the violent crime rate while the second notebook(London Crime Hypothesis Testing Part II.ipynb) to testing the interactions between location/borough and daylight saving for any significant effect on the rate.

My initial assumption is that violent crime rates increase when daylight saving is not in effect, which means that the night is longer. Therefore, our hypothesises are: <br> <br>
Null Hypothesis: The difference between the violent crime rates when daylight saving is and isn't in effect is less than or equal to 0. <br><br>
Alternative Hypothesis: The difference between the violent crime rates when daylight saving is and isn't in effect is greater than 0.<br><br>
We will also assume that a Typer 1 Error rate of 0.05.

## Installation
~~~~~
Packages used:
* Matplotlib
* Numpy
* Pandas
* statsmodels.api
* random
* statsmodels.stats.proportion
~~~~~

## Dataset
If you are interested in downloading the dataset, please click on [this Kaggle link](https://www.kaggle.com/datasets/jboysen/london-crime). There are a total of 13490604 rows in the dataset and 7 columns. Columns include variables such as month, LSOA borough, and major/minor category from Jan 2008-Dec 2016.

## Licensing, Authors, Acknowledgements
I would like to thanks Kaggle and [James Boysen](https://www.kaggle.com/jboysen) for making this dataset publicly available.

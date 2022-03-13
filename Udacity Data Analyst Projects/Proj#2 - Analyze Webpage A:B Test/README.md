# Webpage_ABTest_Analysis_Udacity

Date Created: 11/27/2021

## Project Overview

A/B tests are very commonly performed by data analysts and data scientists. It is important that you get some practice working with the difficulties of these. For this project, I will be working to understand the results of an A/B test run. The company has developed a new web page in order to try and increase the number of users. My goal was to help the company understand if they should implement this new page, keep the old page, or perhaps run the experiment longer to make their decision.

Supporting Material can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/December/5a32c9a0_analyzeabtestresults-2/analyzeabtestresults-2.zip)

## Installation 
You need to be able to work in a Jupyter Notebook on your computer. The following packages (libraries) need to be installed. You can install these packages via conda or pip.
~~~~~~
- Numpy
- Pandas
- Matplotlib
- Statsmodels
- Scipy
~~~~~~
## Project Details
We used three different methods to analyze whether or not to launch a new landing page:

> Probability: Statistics were computed to find out the probabilities of converting regardless of page. These were used to analyze if one page or the other led to more conversions.

> A/B testing: Hypothesis testing was conducted assuming the old page is better unless the new page proves to be definitely better at a Type I error rate of 5%. The data were bootstrapped and sampling distributions were determined for both pages. Conclusions were drawn on conversions for both pages by calculating p-values.

> Logistic regression: Logistic regression was then performed to confirm results of the previous steps. Null and alternative hypotheses associated with this regression model were stated and verified using statsmodel.

For this project, we will use the datasets, 'countries.csv' and 'ab_data.csv'. The original project was turned into Udacity as an HTML file, but I deleted it because the code is the same as in the Jupyter notebook.

## Licensing, Authors, Acknowledgements
I would like to give special thanks to Udacity for giving me the opportunity to work on this project and practice my data analysis skills. 

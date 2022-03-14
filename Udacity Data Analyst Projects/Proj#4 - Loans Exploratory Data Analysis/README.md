# Prosper Loan Data Exploration(Udacity Project)
## by Daniel Chang


## Dataset
This dataset contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate, current loan status, borrower income, among others. The dataset is provided by Prosper via Udacity. You find the file (prosperLoanData.csv) isn't uploaded in the repository since we have added it to the .gitignore file. 


## Summary of Findings
During my bivariate exploration and from out first visualization involving a heat map, I found that the borrower APR and original loan amount were negatively correlated, meaning that the higher the loan, the lower the APR. The relationship between Debt-to-Income Ratio and Stated Monthly Income is also negatively correlated. Furthermore, I also found that the correlation coefficient between the original loan amount and stated monthly income is 0.20, meaning that it's positively correlated. This makes sense since the higher the income, the higher the loan you should be able to acquire.

Moreover, as we move onto different plotting techniques, I found that as a borrower's rating improves, the APR gets lowered drastically. Therefore, we can conclude that the rating has a strong effect on the APR. Those with less desirable statuses(ChargedOff, Past Due, Defaulted) all have higher APR on average.

In my multivariate exploration, an individual's rating has some effect on the relationship between the original loan amount and APR. The relationship gradually turns positive and gets stronger as the rating increases. Term doesn't seem to have any effect on the relationship between the loan amount and APR. One of the more interesting aspects of this exploration phase is my discovery of the term's effect on the relationship between APR and rating. Typically, the APR decreases when the term is longer; for rating B-AA, the longer their term, the higher the APR for each individual level.


## Key Insights for Presentation
For the presentation, I will primarily be focused on features/variables that could affect the Borrower APR. The categorical variables that I am interested in are: 'LoanStatus', 'IncomeVerifiable', 'EmploymentStatus', 'Term', and 'ProsperRating (Alpha)'. The numeric variables that I am interested in are: 'BorrowerAPR', 'StatedMonthlyIncome', 'LoanOriginalAmount', and 'DebtToIncomeRatio'. In this project/presentation, I will examine the relationship between the Borrower APR and several of these variables. For example, some relationships that I examined are APR vs. loan amount and APR vs. rating.

## Licensing, Authors, Acknowledgements
I would like to give special thanks to Udacity and Prosper Loans for giving me the opportunity to do this project and practice my data visualization skills. 

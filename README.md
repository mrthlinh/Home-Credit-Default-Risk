# Table of Contents
1. [Introduction](#Introduction)
- [Feature Selection](#example2): How do you determine feature list and how do you collect data?
- [Exploratory Data Analysis](#third-example): charts and hypothesis testing
- [Methodology](): Details about your procedure
  1. [Classifiers](): Definition and parameters meaning
    - [Dummy Classifiers]() Define a dummy classifier
    - [Logistic Regression]()
    - [Support Vector Machine]()
    - [Ensemble Trees]()
    - [Neural Network]()
  - [Evaluation Criteria](): Definition, strength and weakness
    - [Accuracy]()
    - [Recall, Precision, F1]()
    - [Out of Bag Error]()
    - [10-fold cross validation error]()
  - [Hyper Parameter Tuning]()

- [Results]()
- [References]()


# Project Description
## Description
Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.

Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

While Home Credit is currently using various statistical and machine learning methods to make these predictions, they're challenging Kagglers to help them unlock the full potential of their data. Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity, and repayment calendar that will empower their clients to be successful.

## Data
 __Source__

![](https://github.com/mrthlinh/Home-Credit-Default-Risk/blob/master/Database%20Diagram.png)

__File Explanation__

1. application_{train|test}.csv

   - This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET).
   - Static data for all applications. One row represents one loan in our data sample.

2. bureau.csv

   - All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample).
   - For every loan in our sample, __there are as many rows as number of credits the client had in Credit Bureau before the application date.__

3. bureau_balance.csv

   - Monthly balances of previous credits in Credit Bureau.
   - This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample * # of relative previous credits * # of months where we have some history observable for the previous credits) rows.

4. POS_CASH_balance.csv

   - Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit.
   - This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credits * # of months in which we have some history observable for the previous credits) rows.

5. credit_card_balance.csv

   - Monthly balance snapshots of previous credit cards that the applicant has with Home Credit.
   - This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credit cards * # of months where we have some history observable for the previous credit card) rows.

6. previous_application.csv

   - All previous applications for Home Credit loans of clients who have loans in our sample.
   - There is one row for each previous application related to loans in our data sample.

7. installments_payments.csv

   - Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample.
   - There is a) one row for every payment that was made plus b) one row each for missed payment.
   - One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample.

__Feature List__

__Feature Importance__

## EDA
 - Distribution, (histogram, pie charts...)
 - Imbalance of data
 - Correlation between variables?
 - What did you find from data?
 - Hypothesis testing for feature importance

__EDA example:__

 - https://www.kaggle.com/codename007/home-credit-complete-eda-feature-importance

## Approach

## Preliminary Result


## Task List

__Ongoing__
- [ ] __7/13__ Simple EDA & Simple story with "Previous Application" file
  -*7/6 Note[TN]*: Using https://plot.ly/python/pie-charts/ for code references. Ran into some problem in executing <py.iplot(fig,filename='donut')>. Will update on this problem.
- [ ] __7/13__ Simple EDA & Simple story with "Bureau" file
- [ ] __7/13__ Clean Data and Imputation
- [ ] Prepare framework for Machine learning (sk-learn)
  - [ ] __7/13__ Dummy Classifier / Baseline / Naive Bayes and Submit to Kaggle.
  - [ ] More advanced ML model: Logistic Regression, Random Forest, ...
  - [ ] Small module for result evaluation
- [ ] Hyperparameter based on 10-fold cross validation

__Complete__

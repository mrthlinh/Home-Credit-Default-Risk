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

1. A numbered list
  1. A nested numbered list
  2. Which is numbered
2. Which is numbered
  1. One
  2. Two

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



__Feature List__

__Feature Importance__



## EDA
 - Distribution, (histogram, pie charts...)
 - Imbalance of data
 - Correlation between variables?
 - What did you find from data?

__EDA example:__

 - https://www.kaggle.com/codename007/home-credit-complete-eda-feature-importance

## Approach

## Preliminary Result


## Task List
__Ongoing__
- [ ] Simple EDA & Simple story with "Previous Application" file
- [ ] Simple EDA & Simple story with "Bureau" file
- [ ] Clean Data and Imputation
- [ ] Prepare framework for Machine learning (sk-learn)
  - [ ] Dummy Classifier / Baseline / Naive Bayes
  - [ ] More advanced ML model: Logistic Regression, Random Forest, ...
  - [ ] Small module for result evaluation
- [ ] Hyperparameter based on 10-fold cross validation

__Complete__


# coding: utf-8

# # Home Credit Default Risk_LoadFiles

# This sheet provides exploratory data analysis

# <img src="Database Diagram.png">

# In[1]:


import numpy as np
import pandas as pd


# ### Data Description

# **1) application_{train|test}.csv **
# 
# * This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET).
# * Static data for all applications. One row represents one loan in our data sample.

# In[2]:


Application_Test = pd.read_csv('Data\application_test.csv')


# In[6]:


Application_Test.info()


# In[3]:


Application_Test.head()


# In[4]:


Application_Train = pd.read_csv('application_train.csv')


# In[7]:


Application_Train.info()


# In[5]:


Application_Train.head()


# **2) bureau.csv **
# 
# * All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample).
# * For every loan in our sample, there are as many rows as number of credits the client had in Credit Bureau before the application date.

# In[9]:


Bureau=pd.read_csv('bureau.csv')


# In[12]:


Bureau.info()


# In[11]:


Bureau.head()


# **3) bureau_balance.csv **
# 
# * Monthly balances of previous credits in Credit Bureau.
# * This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample * # of relative previous credits * # of months where we have some history observable for the previous credits) rows.

# In[13]:


Bureau_bal=pd.read_csv('bureau_balance.csv')


# In[14]:


Bureau_bal.info()


# In[15]:


Bureau_bal.head()


# **4) POS_CASH_balance.csv**
# 
# * Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit.
# 
# * This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credits * # of months in which we have some history observable for the previous credits) rows.

# In[17]:


POS=pd.read_csv('POS_CASH_balance.csv')


# In[18]:


POS.info()


# In[19]:


POS.head()


# **5) credit_card_balance.csv**
# 
# * Monthly balance snapshots of previous credit cards that the applicant has with Home Credit.
# * This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credit cards * # of months where we have some history observable for the previous credit card) rows.

# In[20]:


Credit=pd.read_csv('credit_card_balance.csv')


# In[21]:


Credit.info()


# In[22]:


Credit.head()


# **6) previous_application.csv**
# 
# * All previous applications for Home Credit loans of clients who have loans in our sample.
# * There is one row for each previous application related to loans in our data sample.

# In[23]:


Applicant_Hist=pd.read_csv('previous_application.csv')


# In[25]:


Applicant_Hist.info()


# In[24]:


Applicant_Hist.head()


# **7) installments_payments.csv**
# 
# * Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample.
# * There is a) one row for every payment that was made plus b) one row each for missed payment.
# * One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample.

# In[26]:


Pmt=pd.read_csv('installments_payments.csv')


# In[27]:


Pmt.info()


# In[28]:


Pmt.head()


# **8) HomeCredit_columns_description.csv**
# 
# This file contains descriptions for the columns in the various data files.

# In[32]:


#Problem reading this file
#HCDesc=pd.read_csv('HomeCredit_columns_description.csv')


# In[ ]:


#Desc.head()


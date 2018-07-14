# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:00:05 2018

@author: Trang
"""

# # Home Credit Default Risk_EDA



import numpy as np
import pandas as pd

Bureau=pd.read_csv('Data/bureau.csv')
Bureau_bal=pd.read_csv('Data/bureau_balance.csv')
POS=pd.read_csv('Data/POS_CASH_balance.csv')
Credit=pd.read_csv('Data/credit_card_balance.csv')
Applicant_Hist=pd.read_csv('Data/previous_application.csv')
Pmt=pd.read_csv('Data/installments_payments.csv')



import matplotlib.pyplot as plt
%matplotlib inline

import cufflinks as cf
cf.go_offline()

import seaborn as sns

from plotly import __version__
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)


### Missing Value Scan (Will K._Start Here File)
def missing_values(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
    return mis_val_table_ren_columns


missing_values(Applicant_Hist)
missing_values(Bureau)

### 1a Product Combination
#### Try1
Data_pie=Applicant_Hist["PRODUCT_COMBINATION"].value_counts()
fig={
     "data":[{
             "values":Data_pie.values,
             "labels":Data_pie.index,
             "domain":{"x":[0,1]},
             "name":"Product Combination",
             "hoverinfo":"Label+percent+name",
             "hole":0.1,
             "type":"pie"
             }],
     "layout":{
             "title":"Product Combination Type of Previous Application",
             "annotation":[
                     {
                             "font":{
                                     "size":20
                                     },
                                     "showarrow":False,
                                     "text":"Product Combination",
                                     "x":0.1,
                                     "y":0.5
                                     }
                             ]
                      }
}


py.iplot(fig, filename='donut')

#### Try2
#### Note: importing cufflinks and run cf.go_offline() help run the following code
ProductComb=Applicant_Hist["PRODUCT_COMBINATION"].value_counts()
df1a = pd.DataFrame({'labels': ProductComb.index,
                   'values': ProductComb.values
                  })
df1a.iplot(kind='pie',labels='labels',values='values', title='Product Combination', hole = 0.5)

### Heatmap for correlation 
Applicant_Hist_corr=Applicant_Hist.corr()

plt.figure(figsize = (10, 7))
sns.heatmap(Applicant_Hist_corr, cmap = plt.cm.RdYlBu_r, vmin = -0.25, annot = True, vmax = 0.6)
plt.title('Historical HC Applicant Feature Correlation Heatmap')

Bureau_corr=Bureau.corr()
plt.figure(figsize = (10, 7))
sns.heatmap(Bureau_corr, cmap = plt.cm.RdYlBu_r, vmin = -0.25, annot = True, vmax = 0.6)
plt.title('Historical Bureau Applicant Feature Correlation Heatmap')
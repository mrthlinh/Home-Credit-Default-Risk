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

from plotly import __version__
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)




### Product Combination
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



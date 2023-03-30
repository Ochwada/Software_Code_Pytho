#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:50:35 2023

@author: ochwada
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from datetime import datetime, timedelta
from __future__ import division

import chart_studio.plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go


import plotly.offline as pyo
pyo.init_notebook_mode()



#read the data

df = pd.read_excel("data/Online_Retail.xlsx", sheet_name='Online Retail')
df.head(10)

# Converting from string to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#creating YearMonth field for the ease of reporting and visualization
df['InvoiceYearMonth'] = df['InvoiceDate'].map(lambda date: 100*date.year + date.month)

#calculate Revenue for each row and create a new dataframe with YearMonth - Revenue columns
df['Revenue'] = df['UnitPrice'] * df['Quantity']
df_revenue = df.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()
df_revenue.head(10)




#Visualization
#X and Y axis inputs for Plotly graph. We use Scatter for line graphs

plot_df = [go.Scatter(x = df_revenue['InvoiceYearMonth'],
                      y = df_revenue['Revenue'],
                     )]

plot_layout = go.Layout(xaxis= {"type": "category"},
                        title = "Monthly Revenue"
                       )

fig = go.Figure(data = plot_df, layout= plot_layout)
pyoff.iplot(fig)



from __future__ import division

import matplotlib
import pandas as pd
from datetime import datetime, timedelta, date
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

import seaborn as sns
import xgboost as xgb
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import KFold, cross_val_score, train_test_split

import chart_studio.plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go

#initiate plotly
pyoff.init_notebook_mode()
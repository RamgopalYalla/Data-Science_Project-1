#!/usr/bin/env python
# coding: utf-8

# In[7]:


# package for algebra calculations
import numpy as np

# package for processing the data
import pandas as pd

# pakage for data visualization
import seaborn as sns

# matplot libraries
from matplotlib import pyplot as plt
from matplotlib import style

# algorithms and models
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB


# In[10]:


test_df = pd.read_csv("test.csv")
train_df = pd.read_csv("train.csv")


# In[11]:


train_df.info()


# In[19]:


survival:    Survival 
PassengerId: Unique Id of a passenger. 
pclass:    Ticket class     
sex:    Sex     
Age:    Age in years     
sibsp:    # of siblings / spouses aboard the Titanic     
parch:    # of parents / children aboard the Titanic     
ticket:    Ticket number     
fare:    Passenger fare     


    
train_df.describe()


# In[ ]:





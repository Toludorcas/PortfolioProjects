#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[1]:


pip install pandas


# In[2]:


pip install scikit-learn


# In[3]:


pip install matplotlib


# In[4]:


pip install seaborn


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[11]:


data = pd.read_csv(r"C:\Users\USER\Downloads\diabetes.csv")
data


# In[14]:


data.isnull().sum()


# In[15]:


sns.heatmap(data.isnull())


# In[16]:


correlation = data.corr()
print(correlation)


# In[17]:


X = data.drop ("Outcome", axis = 1)
Y = data ["Outcome"]


# In[18]:


X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size = 0.2)


# In[19]:


model = LogisticRegression()
model.fit(X_train, Y_train)


# In[20]:


prediction = model.predict(X_test)


# In[21]:


print(prediction)


# In[22]:


accuracy = accuracy_score(prediction, Y_test)


# In[23]:


print(accuracy)


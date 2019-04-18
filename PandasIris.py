#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
from sklearn import datasets
import seaborn

iris = datasets.load_iris()


# In[5]:





# In[3]:


from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin

km = KMeans(n_clusters= 3)
km.fit(iris)
km.predict(3)


# In[29]:


import pandas as pd
df = pd.DataFrame(iris.data, columns=iris.feature_names)


# In[12]:


df.corr()


# In[40]:


seaborn.heatmap(df.corr(),annot = True,vmin=-1,cmap="PRGn")


# In[41]:


papermak = pandas.read_csv("kamyrdigester.csv")


# In[54]:


cor = papermak.corr()


# In[53]:


matplotlib.rcParams['figure.figsize'] = [20,16]
seaborn.heatmap(papermak.corr(),annot=True,vmin=-1)


# In[ ]:





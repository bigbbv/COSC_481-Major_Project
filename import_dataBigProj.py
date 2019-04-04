#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

file = pd.ExcelFile("SOWC-Statistical-Tables-2017.xlsx");
data = pd.read_excel(file, 'Basic Indicators');
df2 = pd.read_excel(file, 'Nutrition');
data.columns = 
data.loc[1:2].fillna('').apply(' '.join).str.strip()
data = data.ix[3:]
#this currently doesn't work because Row 2 is made of ints. I'm working on a to_str method for rows; Pandas does this very well for columns.


# In[4]:



data


# In[15]:


df2


# In[ ]:





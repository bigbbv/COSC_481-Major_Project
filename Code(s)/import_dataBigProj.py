#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

file = pd.ExcelFile("SOWC Cleaned.xlsx");
dataInd = pd.read_excel(file, 'Basic Indicators');
dataWom = pd.read_excel(file, 'Copy of Women')
#dataInd
#dataInd = dataInd.set_index('TABLE 1. BASIC INDICATORS');


#df2 = pd.read_excel(file, 'Nutrition');


dataInd.columns = dataInd.loc[1].fillna('')
dataWom.columns = dataWom.loc[1].fillna('')

dataInd = dataInd.drop(dataInd.index[0:3])
dataInd = dataInd.drop(dataInd.index[202:])
dataInd = dataInd.set_index('Countries and areas');

dataWom = dataWom.drop(dataWom.index[0:3])
dataWom = dataWom.drop(dataWom.index[202:])
dataWom = dataWom.set_index('Countries and areas');





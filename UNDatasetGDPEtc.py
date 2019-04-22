#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#files = ['Women_In_Parliament.csv', 'Ratio_GB_Education.csv', 'Population_Area_Density.csv','GDP.csv','Employment.csv','Expenditure_on_Education.csv','Crimes.csv']
delet = ['Series', 'Region/Country/Area', 'Footnotes', 'Source', 'Year']
master = pd.read_csv('Internet_Usage.csv',encoding='latin1')
master.columns = master.iloc[0]
master = master[139:]
master = master[master['Year'] > '2016']

delet = ['Series', 'Region/Country/Area', 'Footnotes', 'Source', 'Year']
for title in delet:
    del master[title]
master.columns = ['Country', '% Internet Use']

#filename: Women_In_Parliament
data = pd.read_csv('Women_In_Parliament.csv',encoding='latin1')
data.columns = data.iloc[0]
m = list(data.columns.values)
data = data[139:]
data = data[data['Year'] > '2017']

delet = ['Series', m[4], 'Last Election Date footnote','Footnotes','Source','Region/Country/Area','Year']
for title in delet:
    del data[title]
data.columns = ['Country', '% Women in Govt']

master = pd.merge(master, data, on = 'Country')

    


# In[2]:


#filename: Ratio_GB_Education
data = pd.read_csv('Ratio_GB_Education.csv',encoding='latin1')
data.columns = data.iloc[0]
data = data[229:]
data = data[data['Year'] > '2015']

m = list(data.columns.values)
m[1] = 'Country'
m[4] = 'G to B in Primary Ed'
data.columns = m

delet = [m[0], m[2], m[5], m[6]]
for title in delet:
    del data[title]


#master = pd.merge(master, data, on = 'Country')


# In[3]:


grouped = data.groupby(['Series'])
Prim = grouped.get_group('Ratio of girls to boys in primary education')
master = pd.merge(master,Prim, on = 'Country')


# In[ ]:





# In[4]:


m = list(data.columns.values)
m[2] = 'G to B Secondary Education'
data.columns = m


# In[5]:


grouped = data.groupby(['Series'])
Second = grouped.get_group('Ratio of girls to boys in secondary education')
master = pd.merge(master,Second, on = 'Country')


# In[6]:


m = list(data.columns.values)
m[2] = 'G to B Tertiary Education'
data.columns = m


# In[7]:


grouped = data.groupby(['Series'])
Prim = grouped.get_group('Ratio of girls to boys in tertiary education')
master = pd.merge(master,Prim, on = 'Country')


# In[8]:


del master['Series_x']
del master['Series_y']
del master['Series']


# In[10]:



data = pd.read_csv('Population_Area_Density.csv',encoding='latin1')
data.columns = data.iloc[0]
data = data[900:]
data = data[data['Year'] == '2015']
poss = data.Series.unique().tolist()

delet = ['Region/Country/Area', 'Year','Footnotes','Source']
for title in delet:
    del data[title]
m = list(data.columns.values)
m[0] = 'Country'
data.columns = m

grouped = data.groupby(['Series'])
for item in poss:
    Set = grouped.get_group(item)
    master = pd.merge(master,Set, on = 'Country', how = 'outer')



   
del master['Series_x']
del master['Series_y']


# In[32]:


i = 0
m = list(master.columns.values)
m = m[:6]
for item in poss:
    #use index of poss list to relabel 
    m.append(poss[i])
    i +=1
m

        #then delete the extra columns
        #then rename the columns using data.columns = m


# In[33]:


master = master.iloc[:11]
master.columns = m
master


# In[41]:


data = pd.read_csv('GDP.csv',encoding='latin1')
data.columns = data.iloc[0]
data = data[835:]
data = data[data['Year'] == '2015']
poss = data.Series.unique().tolist()

delet = ['Region/Country/Area', 'Year','Footnotes','Source']
for title in delet:
    del data[title]
m = list(data.columns.values)
m[0] = 'Country'
data.columns = m

grouped = data.groupby(['Series'])
for item in poss:
    Set = grouped.get_group(item)
    master = pd.merge(master,Set, on = 'Country', how = 'outer')



   
del master['Series_x']
del master['Series_y']

i = 0
m = list(master.columns.values)
m = m[:14]
for item in poss:
    #use index of poss list to relabel 
    m.append(poss[i])
    i +=1
m


# In[43]:


master.columns = m
master


# In[44]:


master.to_csv('UNData.csv')


# In[ ]:





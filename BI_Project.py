#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
file = "business-intelligence-project.xlsx"
data = pd.ExcelFile(file)
print(data.sheet_names) #this returns the all the sheets in the excel file


# In[9]:


df = data.parse("Task 1_cleaned")
df.info()


# In[11]:


df.head(10)


# In[ ]:





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


# In[23]:


import statistics
data_mean = statistics.mean(df.Sales)
data_median = statistics.median(df.Sales)
data_mode = statistics.mode(df.Sales)
data_max = max(df.Sales)
data_min = min(df.Sales)
data_stdev = statistics.stdev(df.Sales)


print ("Mean is :", data_mean)
print ("Median is :", data_median)
print ("Mode is :", data_mode)
print ("Maximum Value is :", data_max)
print ("Minimum Value is :", data_min)
print ("Standard Deviation is :", data_stdev)


# In[ ]:





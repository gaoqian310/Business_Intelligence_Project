#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd 
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns

file = "business-intelligence-project.xlsx"
data = pd.ExcelFile(file)
print(data.sheet_names) #this returns the all the sheets in the excel file


# # Task 1

# In[89]:


df = data.parse("Task 1_cleaned")
df.info()


# In[90]:


df.head(10)


# In[91]:


data_mean = st.mean(df.Sales)
data_median = st.median(df.Sales)
data_mode = st.mode(df.Sales)
data_max = max(df.Sales)
data_min = min(df.Sales)
data_stdev = st.stdev(df.Sales)


print ("Mean is :", data_mean)
print ("Median is :", data_median)
print ("Mode is :", data_mode)
print ("Maximum Value is :", data_max)
print ("Minimum Value is :", data_min)
print ("Standard Deviation is :", data_stdev)


# ## Virtrualizaiton the distribution of the sales data

# In[92]:




sns.set_theme(style="whitegrid")
plt.figure (figsize=(15,2))

ax = sns.boxplot(orient = "h", data=df.Sales)
ax = sns.swarmplot(orient = "h",data=df.Sales, color=".25")


# In[93]:


plt.figure (figsize=(15,6))
sns.kdeplot(data=df.Sales)


# # Task 2

# In[94]:


df = data.parse("Task 2_cleaned")
df.info()


# In[95]:


df.head()


# In[97]:


df["Customer Conversion Rate"] = df["Number of Customer Made a Purchased"]/df["Total Number of Customer Visited"]
df.head()


# In[100]:


data_mean = st.mean(df["Customer Conversion Rate"])
data_median = st.median(df["Customer Conversion Rate"])
data_mode = st.mode(df["Customer Conversion Rate"])
data_range = max(df["Customer Conversion Rate"])-min(df["Customer Conversion Rate"])
data_stdev = st.stdev(df["Customer Conversion Rate"])


print ("Mean is :", data_mean)
print ("Median is :", data_median)
print ("Mode is :", data_mode)
print ("Range(max-min) is :", data_range)
print ("Standard Deviation is :", data_stdev)


# In[ ]:





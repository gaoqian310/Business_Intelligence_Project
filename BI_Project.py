#!/usr/bin/env python
# coding: utf-8

# In[162]:


import pandas as pd 
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

file = "business-intelligence-project.xlsx"
data = pd.ExcelFile(file)
print(data.sheet_names) #this returns the all the sheets in the excel file


# # Task 1

# In[163]:


df1 = data.parse("Task 1_cleaned")
df1.info()


# In[164]:


df1.head(10)


# In[165]:


data_mean = st.mean(df1.Sales)
data_median = st.median(df1.Sales)
data_mode = st.mode(df1.Sales)
data_max = max(df1.Sales)
data_min = min(df1.Sales)
data_stdev = st.stdev(df1.Sales)
data_skew = skew(df1.Sales)

print ("Mean is :", data_mean)
print ("Median is :", data_median)
print ("Mode is :", data_mode)
print ("Maximum Value is :", data_max)
print ("Minimum Value is :", data_min)
print ("Standard Deviation is :", data_stdev)
print ("Skewness is :", data_skew)


# ## Virtrualizaiton the distribution of the sales data

# In[166]:


sns.set_theme(style="whitegrid")
plt.figure (figsize=(15,2))

ax = sns.boxplot(orient = "h", data=df1.Sales)
ax = sns.swarmplot(orient = "h",data=df1.Sales, color=".25")


# In[167]:


plt.figure (figsize=(15,6))
sns.kdeplot(data=df1.Sales)
plt.show()


# #### Conclusion
# From the calculations and two charts above, we can see the spread from 338.6 to 9676
# 
# The mean is 4444.58
# 
# skewness is 0.17
# 

# # Task 2

# In[168]:


df2 = data.parse("Task 2_cleaned")
df2.info()


# In[169]:


df2.head(10)


# In[170]:


df2["Customer Conversion Rate"] = df2["Number of Customer Made a Purchased"]/df2["Total Number of Customer Visited"]
df2.head()


# In[179]:


data_mean = st.mean(df2["Customer Conversion Rate"])
data_median = st.median(df2["Customer Conversion Rate"])
data_mode = st.mode(df2["Customer Conversion Rate"])
data_range = max(df2["Customer Conversion Rate"])-min(df["Customer Conversion Rate"])
data_stdev = st.stdev(df2["Customer Conversion Rate"])

print ("Mean is :", data_mean)
print ("Median is :", data_median)
print ("Mode is :", data_mode)
print ("Range(max-min) is :", data_range)
print ("Standard Deviation is :", data_stdev)


# In[172]:


sns.set_theme(style="whitegrid")
plt.figure (figsize=(15,2))

ax = sns.boxplot(orient = "h", data=df2["Customer Conversion Rate"])
ax = sns.swarmplot(orient = "h",data=df2["Customer Conversion Rate"], color=".2")


# #### Conclusion
# From the plot above, we can tell that the company is not proformce very well. 
# 
# The median is only 0.1275 which indicating that among all the stores, more than half of the store are below national benchmark.

# ## Task 3

# In[173]:


df3 = data.parse("Task 3_cleaned")
df3.info()


# In[174]:


df3.head(10)


# In[180]:


x = df3["Ice Crem Sale (X)"]
y = df3["Sunglasses Sold (Y)"]

plt.xlabel('Ice Crem Sale')
plt.ylabel('Sunglasses Sold')

plt.scatter(x, y)
plt.show()


# #### Method 1

# In[176]:


np.corrcoef(df3["Ice Crem Sale (X)"], df3["Sunglasses Sold (Y)"])


# #### Method 2

# In[177]:


df3["Ice Crem Sale (X)"].corr(df3["Sunglasses Sold (Y)"])


# In[178]:


df3["Sunglasses Sold (Y)"].corr(df3["Ice Crem Sale (X)"])


# #### Conclusion
# the Ice cream sales and Sanglasses sold are positive correlated, and the correlation coefficient is about 0.97.
# 
# But positive correlation doesn't mean causation, a controlled study is usually the effective way to determine causation.
# 
# In this case, the causation for both sales increase at same time is most likely the high temperature / hot weather.

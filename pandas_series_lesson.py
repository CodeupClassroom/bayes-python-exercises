#!/usr/bin/env python
# coding: utf-8

# # Pandas
# - Data Analysis library
# - Primary tool for data wrangling and preparation

# ## Two Main Components of Pandas
# #### 1. Series are one dimensional representations of data (Columns)
# 
# #### 2. Dataframes are the 2d data structures in pandas

# ### Introducing pandas Series

# In[2]:


import pandas as pd


# In[9]:


numbers = [3.141, 4, 10, 12, 23, -2, -1, 0, 0, 2, 0, -6, 3, 3, 3, 3, -7]


# In[10]:


numbers = pd.Series(numbers)


# In[11]:


type(numbers)


# In[12]:


print(numbers)


# In[8]:


numbers.index


# In[14]:


numbers.name = "My list of numbers"
numbers


# In[15]:


vegetables = ["brussel sprouts", "yam", "arugala"]
vegetables = pd.Series(vegetables)
vegetables


# In[16]:


pd.Series((1, 2))


# In[28]:


import numpy as np
numbers = np.arange(1000000)
numbers = pd.Series(numbers)
# numbers.astype('str')
numbers


# In[18]:


numbers.head()


# In[20]:


numbers.head(7)


# In[25]:


numbers.tail()


# In[32]:


numbers * numbers


# In[33]:


get_ipython().run_line_magic('timeit', 'numbers * numbers')


# In[35]:


numbers[numbers % 2 == 0] # same syntax as numpy


# In[37]:


vegetables == "yam"


# In[39]:


vegetables[vegetables == "yam"]


# In[42]:


(vegetables != "yam").any() # do any of the values in the series match this comparison


# In[43]:


(vegetables == "eggplant").any()


# In[46]:


(numbers % 2 == 0).any()


# In[47]:


print((numbers > 0).all()) # not all are negative
print((numbers > 0).any()) # not one is ?


# In[49]:


(numbers == "3").any()


# In[50]:


numbers = [3.141, 4, 10, 12, 23, -2, -1, 0, 0, 2, 0, -6, 3, 3, 3, 3, -7]


# In[52]:


numbers = pd.Series(numbers)
numbers


# In[60]:


x = numbers.value_counts()
type(x)
print("index is the list of unique values", x.index)
print("actual value counts", x.values)
print(x)


# In[62]:


numbers * numbers


# In[66]:


x = numbers * pd.Series([1, 2, 3])
x


# In[67]:


x.mean()


# In[68]:


x.sum()


# In[ ]:





# In[54]:


numbers.unique()


# In[ ]:





# In[70]:


vowels = list('aeiou')
letters = list('abcdefghijk')
letters_series = pd.Series(letters)
letters_series


# In[71]:


letters_series.isin(vowels)


# In[76]:


up_to_hundred_thousand = pd.Series(np.arange(100_000))
output = up_to_hundred_thousand.isin(numbers)
output.head(20)


# In[77]:


numbers


# In[78]:


numbers.mean()


# In[79]:


numbers.median()


# In[80]:


numbers.describe()


# In[81]:


vegetables.describe()


# In[ ]:





# In[41]:


print("Count is", numbers.count())
print("Sum is", numbers.sum())
print("Mean is", numbers.mean())


# In[42]:


print("Median is", numbers.median())
print("Minimum value is", numbers.min())
print("Maximum value is", numbers.max())
print("Mode is", numbers.mode())


# In[36]:


numbers.value_counts()


# In[6]:


numbers.value_counts().plot.bar()


# In[50]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits.name = "My List of Fruits"


# In[51]:


fruits


# In[38]:





# In[14]:


# Capitalize the series of strings


# In[15]:





# In[17]:





# In[52]:


fruits.unique()


# In[ ]:





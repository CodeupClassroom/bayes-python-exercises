#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd


# In[21]:


numbers = pd.Series(range(1000))


# In[22]:


numbers


# In[23]:


def even_or_odd(number):
    if number % 2 == 0:
        return 'even'
    else: 
        return 'odd'


# In[24]:


even_or_odd(23)


# In[25]:


even_or_odd


# In[26]:


# .apply takes in a function definition into its parens
numbers.apply(even_or_odd)


# In[27]:


numbers


# In[ ]:





# In[28]:


len("banana")


# In[29]:


vegetables = pd.Series(["eggplant", "tomato", "leek", "palm hearts", "artichoke", "okra"])


# In[30]:


vegetables


# In[31]:


vegetables.apply(len)


# In[35]:


def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count


# In[36]:


count_vowels("banana")


# In[39]:


print(vegetables)
print(vegetables.apply(count_vowels))


# In[41]:


def count_g(word):
    return word.count("g")

vegetables.apply(count_g)


# In[42]:


count_g = lambda x: x.count("g")


# In[43]:


# lambdas
# count the letter "g" in each word
vegetables.apply(count_g)


# In[44]:


vegetables


# In[45]:


vegetables.apply(lambda x: x.upper())


# In[46]:


vegetables.str.upper()


# In[47]:


vegetables.str.capitalize()


# In[48]:


vegetables.str.count("g")


# In[49]:


vegetables.str.replace("a", "z")


# In[50]:


prices = pd.Series(["$8.99", "$4.99"])


# In[51]:


prices


# In[54]:


vegetables[vegetables != "leek"]


# In[56]:


def is_even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


# In[59]:


mask = numbers.apply(is_even_or_odd)


# In[60]:


numbers[mask]


# In[62]:


s = pd.Series(list(range(15)))
s


# In[63]:


pd.cut(s, 3)


# In[65]:


pd.cut(s, 2)


# In[76]:


pd.cut(s, [float("-inf"), 3, 4, 12, float("inf")])


# In[69]:


45ms


# In[77]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[78]:


s.plot()


# In[79]:


s.plot.hist()


# In[82]:


pd.Series(['a', 'b', 'a', 'c', 'b', 'a', 'd', 'a']).value_counts().plot.bar(color="firebrick", width=.9)


# In[86]:





# In[ ]:





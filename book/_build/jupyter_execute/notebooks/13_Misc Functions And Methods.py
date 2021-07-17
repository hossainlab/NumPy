#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


salaries = np.genfromtxt('data/salary.csv', delimiter=',')


# In[4]:


salaries


# In[5]:


salaries.shape


# ### argmax

# Returns the indices of the maximum values along an axis.

# In[6]:


np.argmax(salaries)


# In[7]:


salaries[246]


# ### argmin

# Returns the indices of the minimum values along an axis.

# In[8]:


np.argmin(salaries)


# In[9]:


salaries[282]


# ### argsort

# Returns the indices that would sort an array.

# In[45]:


np.argsort(salaries)


# ##### Specify a sorting algorithm
# Perform an indirect sort along the given axis using the algorithm specified by the kind keyword. It returns an array of indices of the same shape as a that index data along the given axis in sorted order.

# In[46]:


np.argsort(salaries,kind='mergesort')


# ##### View the sorted salary values

# In[10]:


salaries[np.argsort(salaries,kind='mergesort')]


# The functions <b> max , min , sort </b> gives the respective elements itself instead of indices.

# ### where

# The where() function returns the indices of elements in an input array where the given condition is satisfied.

# In[11]:


greater_than_100 = np.where(salaries > 100000)


# In[12]:


greater_than_100


# In[15]:


len(greater_than_100[0])


# In[55]:


salaries[greater_than_100]


# ### extract
# The extract() function returns the elements satisfying any condition

# ##### Start off by defining a condition

# In[16]:


condition = salaries > np.mean(salaries)


# ##### Use the condition in the extract function

# In[17]:


np.extract(condition, salaries)


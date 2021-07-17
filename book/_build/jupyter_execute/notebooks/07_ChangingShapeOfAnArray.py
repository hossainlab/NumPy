#!/usr/bin/env python
# coding: utf-8

# ## Array Shape Manipulation

# In[1]:


import numpy as np


# ### 1. Flattening

# In[2]:


a = np.array([("Germany","France", "Hungary","Austria"),
              ("Berlin","Paris", "Budapest","Vienna" )]) 


# In[3]:


a


# In[4]:


a.shape


# #### The ravel() function
# The primary functional difference is that flatten is a method of an ndarray object and hence can only be called for true numpy arrays. In contrast ravel() is a library-level function and hence can be called on any object that can successfully be parsed. For example ravel() will work on a list of ndarrays, while flatten will not.

# In[5]:


a.ravel()


# ##### T gives transpose of an array

# In[6]:


a.T   


# In[7]:


a.T.ravel()


# ### 2. Reshaping

# reshape() gives a new shape to an array without changing its data.

# In[8]:


a.shape


# In[9]:


a.reshape(4,2)


# In[10]:


np.arange(15).reshape(3,5)


# In[16]:


np.arange(15).reshape(5,3)


# ##### The reshape() dimensions needs to match the number of values in the array
# Reshaping a 15-element array to an 18-element one will throw an error

# In[11]:


np.arange(15).reshape(3,6)


# #### Specify only one dimension (and infer the others) when reshaping
# Another way we can reshape is by metioning only one dimension, and -1. -1 means that the length in that dimension is inferred

# In[12]:


countries = np.array(["Germany","France", "Hungary","Austria","Italy","Denmark"])
countries


# ##### Here the unspecified value is inferred to be 2

# In[13]:


countries.reshape(-1,3) 


# ##### Here the unspecified value is inferred to be 3

# In[14]:


countries.reshape(3,-1) 


# ##### If the values of the dimensions are not factors of the number of elements, there will be an error

# In[15]:


countries.reshape(4,-1)


# In[ ]:





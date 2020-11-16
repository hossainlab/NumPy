#!/usr/bin/env python
# coding: utf-8

# # Setting and Slicing Array Elements

# In[1]:


import numpy as np 


# ## Array Slicing

# In[2]:


# Create an array 
A = np.array([0, 1, 2, 3])
print(A)


# ### Positive Indexing
# Select `nth` element of an array by using `var[position]`

# In[3]:


# Select 0th element of `A`
A[0]


# In[4]:


# Select 1st element of `A`
A[1]


# ### Negative Indexing

# In[5]:


# Select last element of `A`
A[-1]


# In[6]:


A[-2]


# Extract a Portion of a Sequence by specifying a lower and upper bound. The lower bound element is `included`, but the upper-bound element is `not included`. Mathematically: [lower, upper]. The stop value specifies the stride between elements.
# 

# In[7]:


B = np.array([0, 1, 2, 3, 4, 5, 6, 7])


# In[8]:


# indices
B[1:3]


# In[9]:


# negative indices work also
B[1:-2]


# In[10]:


B[-4:3]


# Omitted boundaries are assumed to be the beginning (or end) of the list

# In[11]:


# grab first theree elements 
B[:3]


# In[12]:


# grab last two elements 
B[-2:]


# In[13]:


# grab every other elements 
B[::2]


# ## 2D Array Slicing

# In[14]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# In[15]:


# grab 1st row and 1st element 
arr[0, 0]


# In[16]:


# same as above
arr[0, 2]


# In[17]:


# negative indexing 
arr[0, -1]


# In[18]:


# select all rows and last element
arr[:, 2]


#!/usr/bin/env python
# coding: utf-8

# # Array Slicing and Subsetting

# In[1]:


# import numpy 
import numpy as np 


# ## 1D Array Slicing
# - 1D array at index `i`
# - Returns the `ith` element of an array
# - **Syntax:** `array[i]`

# In[2]:


# Create an 1D arary 
A1 = np.array([11, 22, 34, 12, 15])


# In[3]:


# Select ith element of A1 
A1[1]


# In[4]:


# Negative indexing 
A1[-1]


# ## 2D Array Slicing
# - 2D array at index `[i][j]`
# - Returns the `[i][j]` element of an array
# - **Syntax:** `array[i][j]`

# In[5]:


# Create an 2D array 
A2 = np.array([[0, 1, 3], [4, 6, 7]])


# In[6]:


# Select the first row of A2 
A2[0]


# In[7]:


# Select the first element of first row 
A2[0][0]


# __Note__
# 
# - First, `A2[0]` = [0, 1, 3], which is the first row of array `A2`
# - Second, `A2[0]` select the first element of first row. 

# In[8]:


# Select the second row of A2 
A2[1]


# In[9]:


# Select the 3rd element of second row 
A2[1][2]


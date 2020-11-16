#!/usr/bin/env python
# coding: utf-8

# # Array Operations

# In[1]:


# import numpy 
import numpy as np


# ## Copy
# - Copies array to new memory
# - **Syntax:** `np.copy(array)`

# In[2]:


# create an array `A1`
A1 = np.arange(10)
print(A1)


# In[3]:


# copy `A1` into A2 
A2 = np.copy(A1)
print(A2)


# ## View
# - Creates view of array elements with type(dtype)
# - **Syntax:** `array.view(np.dtype)`

# In[4]:


# view of array A2 
A3 = A2.view(np.float16)
print(A3)


# ## Sorting
# - Returns a sorted copy of an array.
# - **Syntax:** `array.sort()`
#     - element-wise sorting(default) 
#     - axis = 0; row
#     - axis = 1; column
# ![Axis](../img/axis.png)

# In[5]:


# Unsorted array
A4 = np.array([9, 2, 3,1, 5, 10])
print(A4) 


# In[6]:


# Call sort function
A4.sort()
print(A4)


# In[7]:


# Row and column unsorted
A5 = np.array([[4, 1, 3], [9, 5, 8]])
print(A5) 


# In[8]:


# Apply sort function on column axis=1
A5.sort(axis=1)
print(A5)


# ## Flatten: Flattens 2D array to 1D array
# 

# In[9]:


# 2D array
A6 = np.array([[4, 1, 3], [9, 5, 8]])
# 1D array 
A6.flatten()


# ## Transpose: Transposes array (rows become columns and vice versa)
# 

# In[10]:


A7 = np.array([[4, 1, 3], [9, 5, 8]])
A7


# In[11]:


# Transpose A7 
A7.T


# ## Reshape: Reshapes arr to `r` rows, `c` columns without changing data
# ![Reshape](../img/reshape.png)

# In[12]:


A8 = np.array([(8,9,10),(11,12,13)])
A8


# In[13]:


# Reshape --> 3x4
A8.reshape(3,2)


# ## Resize:  Changes arr shape to `rxc` and fills new values with 0
# 

# In[14]:


A9 = np.array([(8,9,10),(11,12,13)])
A9


# In[15]:


# Resize 
A9.resize(3, 2)
A9


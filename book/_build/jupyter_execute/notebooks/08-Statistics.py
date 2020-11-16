#!/usr/bin/env python
# coding: utf-8

# # Statistics

# In[1]:


import numpy as np 


# In[36]:


# 1D array 
A = np.arange(20)
print(A)


# In[39]:


A.ndim


# In[37]:


# 2D array 
A2 = np.array([[11, 12, 13], [21, 22, 23]])
print(A2)


# In[40]:


A2.ndim


# ## Sum 
# - Sum of array elements over a given axis.
#     - **Syntax:** `np.sum(array); array-wise sum`
#     - **Syntax:** `np.sum(array, axis=0); row-wise sum`
#     - **Syntax:** `np.sum(array, axis=1); column-wise sum`

# ![](../img/axis.jpg)
# Axis 0 is thus the first dimension (the "rows"), and axis 1 is the second dimension (the "columns")

# In[41]:


# sum of 1D array 
np.sum(A1)


# In[42]:


# array-wise sum of 2D array 
np.sum(A2)


# In[43]:


# sum of 2D array(axis=0, row-wise sum)
np.sum(A2, axis=0)


# In[44]:


# sum of 2D array(axis=1, column-wise sum)
np.sum(A2, axis=1)


# ## Mean 
# - Compute the median along the specified axis.
# - Returns the average of the array elements. The average is taken over the flattened array by default,  otherwise over the specified axis. `float64` intermediate and return values re used for integer inputs.
# 
#     - **Syntax:** `np.mean(array); array-wise mean`
#     - **Syntax:** `np.mean(array, axis=0); row-wise mean`
#     - **Syntax:** `np.mean(array, axis=1); column-wise mean`

# In[45]:


# compute the average of array `A`
np.mean(A)


# In[46]:


# mean of 2D array(axis=0, row-wise)
np.mean(A2, axis=0)


# In[47]:


# mean of 2D array(axis=1, column-wise)
np.mean(A2, axis=1)


# ## Median
# - Compute the median along the specified axis.
# - Returns the median of the array elements.
#     
#     - **Syntax:** `np.median(array); array-wise median`
#     - **Syntax:** `np.median(array, axis=0); row-wise median`
#     - **Syntax:** `np.median(array, axis=1); column-wise median`

# In[48]:


# compute the meadian of `A`
np.median(A)


# In[21]:


# median of 2D array(axis=0, row-wise)
np.median(A2, axis=0)


# In[22]:


# median of 2D array(axis=1, column-wise)
np.median(A2, axis=1)


# ## Minimum 
# - Return the minimum of an array or minimum along an axis.
#      
#     - **Syntax:** `np.min(array); array-wise min`
#     - **Syntax:** `np.min(array, axis=0); row-wise min`
#     - **Syntax:** `np.min(array, axis=1); column-wise min`

# In[59]:


# minimum value of `A`
np.min(A)


# In[61]:


# minimum value of A2(axis=0, row-wise)
np.min(A2, axis=0)


# In[62]:


# minimum value of A2(axis=1, column-wise)
np.min(A2, axis=1)


# ## Minimum 
# - Return the maximum of an array or minimum along an axis.
#      
#     - **Syntax:** `np.max(array); array-wise max`
#     - **Syntax:** `np.max(array, axis=0); row-wise max`
#     - **Syntax:** `np.max(array, axis=1); column-wise max`

# In[63]:


# maxiumum value of `A`
np.max(A)


# In[64]:


# maxiumum value of A2(axis=0, row-wise)
np.max(A2, axis=0)


# In[65]:


# maxiumum value of A2(axis=1, column-wise)
np.max(A2, axis=1)


# ## Range 
# - **Syntax:** `np.max(array) - np.min(array)`

# In[66]:


r = np.max(A) - np.min(A)
print(r)


# ## Standard Deviation
# - Compute the standard deviation along the specified axis.
# - Returns the standard deviation, a measure of the spread of a distribution, of the array elements. The standard deviation is computed for the
# flattened array by default, otherwise over the specified axis.
#     - **Syntax:** `np.std(array); array-wise std`
#     - **Syntax:** `np.std(array, axis=0); row-wise std`
#     - **Syntax:** `np.std(array, axis=1); column-wise std`

# In[49]:


# compute the standard deviation of `A`
np.std(A)


# In[25]:


# standard deviation of 2D array(axis=0, row-wise)
np.std(A2, axis=0)


# In[27]:


# standard deviation of 2D array(axis=1, column-wise)
np.std(A2, axis=1)


# ## Variance
# - Compute the variance along the specified axis.
# - Returns the variance of the array elements, a measure of the spread of a
#   distribution.  The variance is computed for the flattened array by
#   default, otherwise over the specified axis.
#     - **Syntax:** `np.var(array); array-wise var`
#     - **Syntax:** `np.var(array, axis=0); row-wise var`
#     - **Syntax:** `np.var(array, axis=1); column-wise var`

# In[50]:


# compute the variance of `A`
np.var(A)


# In[32]:


# variance of 2D array(axis=0, row-wise)
np.std(A2, axis=0)


# In[33]:


# variance of 2D array(axis=1, column-wise)
np.std(A2, axis=0)


# ## Quantile
# - Compute the q-th quantile of the data along the specified axis.
#     - **Syntax:** `np.quantile(array); array-wise quantile`
#     - **Syntax:** `np.quantile(array, axis=0); row-wise quantile`
#     - **Syntax:** `np.quantile(array, axis=1); column-wise quantile`

# In[55]:


# 25th percentile of `A`
np.quantile(A, 0.25)


# In[56]:


# 50th percentile of `A2`(axis=0)
np.quantile(A2, 0.5, axis=0)


# In[57]:


# 75th percentile of `A2`(axis=1)
np.quantile(A2, 0.75, axis=1)


# ## Correlation Coefficient

# In[68]:


# documentation 
np.info(np.corrcoef)


# In[70]:


# compute Correlation Coefficient
np.corrcoef(A2)


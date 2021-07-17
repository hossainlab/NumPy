#!/usr/bin/env python
# coding: utf-8

# # Array Operations

# In[ ]:


# import numpy 
import numpy as np


# ## Copy
# - Copies array to new memory
# - **Syntax:** `np.copy(array)`

# In[ ]:


# create an array `A1`
A1 = np.arange(10)
print(A1)


# In[ ]:


# copy `A1` into A2 
A2 = np.copy(A1)
print(A2)


# ## View
# - Creates view of array elements with type(dtype)
# - **Syntax:** `array.view(np.dtype)`

# In[ ]:


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

# In[ ]:


# Unsorted array
A4 = np.array([9, 2, 3,1, 5, 10])
print(A4) 


# In[ ]:


# Call sort function
A4.sort()
print(A4)


# In[ ]:


# Row and column unsorted
A5 = np.array([[4, 1, 3], [9, 5, 8]])
print(A5) 


# In[ ]:


# Apply sort function on column axis=1
A5.sort(axis=1)
print(A5)


# ## Flatten: Flattens 2D array to 1D array
# 

# In[ ]:


# 2D array
A6 = np.array([[4, 1, 3], [9, 5, 8]])
# 1D array 
A6.flatten()


# ## Transpose: Transposes array (rows become columns and vice versa)
# 

# In[ ]:


A7 = np.array([[4, 1, 3], [9, 5, 8]])
A7


# In[ ]:


# Transpose A7 
A7.T


# ## Reshape: Reshapes arr to `r` rows, `c` columns without changing data
# ![Reshape](../img/reshape.png)

# In[ ]:


A8 = np.array([(8,9,10),(11,12,13)])
A8


# In[ ]:


# Reshape --> 3x4
A8.reshape(3,2)


# ## Resize:  Changes arr shape to `rxc` and fills new values with 0
# 

# In[ ]:


A9 = np.array([(8,9,10),(11,12,13)])
A9


# In[ ]:


# Resize 
A9.resize(3, 2)
A9


# In[1]:


import numpy as np


# ## Arithmetic Operations

# If the dimensions of two arrays are dissimilar, element-to-element operations are not possible. However, operations on arrays of non-similar shapes is still possible in NumPy, because of the broadcasting capability. We will see what broadcasting is in the upcoming lessons.

# In[9]:


a = np.array([10,10,10])
b = np.array([5,5,5])


# In[3]:


a + b


# In[4]:


a - b


# In[5]:


a * b


# In[6]:


a / b


# In[7]:


a % 3  


# In[8]:


a < 35


# In[9]:


a > 25


# In[10]:


a ** 2


# ## dot function or method

# In[5]:


A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0], [3,4]] )

print('A:\n', A)
print('B:\n', B)


# #### This gives element-wise multiplication

# In[12]:


A * B


# #### This gives the matrix multiplication

# In[13]:


A.dot(B)


# In[14]:


np.dot(A,B)


# ## Modifying an existing array rather than create a new one

# In[10]:


a  *= 3
a


# In[11]:


b += a
b


# ## Unary Operators

# In[12]:


ages = np.array([12,15,18,20])


# In[13]:


ages.sum()


# In[14]:


ages.min()


# In[15]:


ages.max()


# By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the axis parameter you can apply an operation along the specified axis of an array

# In[16]:


numbers = np.arange(12).reshape(3,4)
numbers


# #### Row and column operations
# In a 2D array axis #0 represents columns. Axis #1 refers to rows

# #### Sum up each column

# In[19]:


numbers.sum(axis=0) 


# #### Sum up each row

# In[20]:


numbers.sum(axis=1)


# #### Minimum of each row

# In[21]:


numbers.min(axis=1) 


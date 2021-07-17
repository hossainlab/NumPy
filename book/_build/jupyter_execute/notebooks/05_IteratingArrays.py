#!/usr/bin/env python
# coding: utf-8

# # Iterating Arrays 

# In[1]:


import numpy as np


# ### 1D Arrays

# In[7]:


a = np.arange(11)**2


# In[8]:


a


# In[12]:


# Iteratating over an array 
for i in a:
    print(i)


# In[13]:


# Iteratating over an array 
for i in a:
    print(i * 2)


# ## Multi-Dimensional Arrays

# Iterating over multidimensional arrays is done with respect to the first axis:
# 
# 

# In[14]:


students = np.array([['Alice','Beth','Cathy','Dorothy'],
                     [65,78,90,81],
                     [71,82,79,92]])


# ##### Each iteration will be over the rows of the array

# In[15]:


for i in students:
    print('i = ', i)


# ### Flatten a multi-dimensional array
# If one wants to perform an operation on each element in the array, one can use the flatten function which will flatten the array to a single dimension. <br />
# By default, the flattening will occur row-wise (also knows as C order)

# In[16]:


for element in students.flatten():
    print(element)


# ##### Fortran order flattening
# To flatten a 2D array column-wise, use the Fortran order

# In[17]:


for element in students.flatten(order='F'):
    print(element)


# ## nditer
# Efficient multi-dimensional iterator object to iterate over arrays

# In[18]:


x = np.arange(12).reshape(3,4)
x


# ##### Default iteration behavior is C order
# This is row-wise iteration, similar to iterating over a C-order flattened array

# In[19]:


for i in np.nditer(x):
    print(i)


# ##### Fortran order
# This is like iterating over an array which has been flattened column-wise

# In[20]:


for i in np.nditer(x, order = 'F'): 
    print(i)


# #### Flags
# There are a number of flags which we can pass as a list to nditer. Many of these involve setting buffering options <br />
# If we want iterate over each column, we can use the flag argument with value 'external_loop'

# In[21]:


for i in np.nditer(x, order = 'F', flags = ['external_loop']): 
    print(i)


# ### Modifying Array Values

# By default, the nditer treats the input array as a read-only object. To modify the array elements, you must specify either read-write or write-only mode. This is controlled with per-operand flags.

# ##### Writing on a read-only array results in an error

# In[22]:


for arr in np.nditer(x):
    arr[...] = arr * arr


# ##### We set the ops_flag to make the array read-write

# In[23]:


for arr in np.nditer(x, op_flags = ['readwrite']):
    arr[...] = arr * arr


# In[24]:


x


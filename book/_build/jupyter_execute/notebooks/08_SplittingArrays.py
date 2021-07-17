#!/usr/bin/env python
# coding: utf-8

# ## Splitting Arrays

# In[1]:


import numpy as np


# ### 1.split

# Split an array into multiple sub-arrays. By specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur

# <b>split(array, indices_or_sections, axis=0)</b> 

# In[2]:


x = np.arange(9)


# In[3]:


x


# In[5]:


print('Split the array in 3 equal-sized subarrays:' )
np.split(x, 3)


# #### The number of splits must be a divisor of the number of elements
# Or Numpy will complain that an even split is not possible

# In[19]:


np.split(x, 4)


# In[6]:


print('Split the array at positions indicated in 1-D array:' )
np.split(x,[4,7])


# ### 2.hsplit

# The numpy.hsplit is a special case of split() function where axis is 1 indicating a horizontal split regardless of the dimension of the input array. <br />
# In this example, the split will be performed along a column

# In[7]:


y = np.array([("Germany","France", "Hungary","Austria"),
              ("Berlin","Paris", "Budapest","Vienna" )]) 


# In[8]:


y


# In[9]:


p1, p2 = np.hsplit(y, 2)


# In[10]:


print(p1)


# In[11]:


print(p2)


# In[12]:


np.hsplit(y,4)


# In[18]:


np.hsplit(y,3)


# ### 3.vsplit

# vsplit splits along the vertical axis

# In[15]:


p_1,p_2 = np.vsplit(y, 2)


# In[16]:


print(p_1)


# In[17]:


print(p_2)


# ### Array Unpacking

# An alternative approach is array unpacking. In this example, we unpack the array into two variables. The array unpacks by row i.e Unpacking "unpacks" the first dimensions of an array 

# In[20]:


countries,capitals = y


# In[21]:


print('Countries: ')
print(countries)
print('Capitals: ')
print(capitals)


# To get the columns, just transpose the array.

# In[22]:


b1,b2,b3,b4 = y.T


# In[23]:


print("b1: ")
print(b1)
print("b2: ")
print(b2)
print("b3: ")
print(b3)
print("b4: ")
print(b4)


# We can not use the following code, reason being the first dimension of array now contains 4 rows. If we want to split in 2 arrays horizontally we should use <b>split</b> or <b>hsplit</b>.

# In[24]:


z1,z2 = y.T


# In[ ]:





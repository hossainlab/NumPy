#!/usr/bin/env python
# coding: utf-8

# ## Vector Stacking
# 

# In[2]:


import numpy as np


# ### 1. concatenate

# The arrays must have the same shape, except in the dimension corresponding to axis. The default axis along which the arrays will be joined is 0.

# In[3]:


x = np.array([["Germany","France"],["Berlin","Paris"]])
y = np.array([["Hungary","Austria"],["Budapest","Vienna"]])


# In[4]:


print(x)
print(x.shape)


# In[5]:


print(y)
print(y.shape)


# ##### The default is row-wise concatenation for a 2D array

# In[6]:


print('Joining two arrays along axis 0')
np.concatenate((x,y))


# ##### Column-wise

# In[7]:


print('Joining two arrays along axis 1')
np.concatenate((x,y), axis = 1)


# ### 2. stack

# In[69]:


a = np.array([1, 2, 3])
b = np.array([2, 3, 4])


# In[70]:


np.stack((a, b))


# In[8]:


studentId = np.array([1,2,3,4])
name   = np.array(["Alice","Beth","Cathy","Dorothy"])
scores  = np.array([65,78,90,81])


# In[9]:


np.stack((studentId, name, scores))


# In[10]:


np.stack((studentId, name, scores)).shape


# In[11]:


np.stack((studentId, name, scores), axis =1)


# In[12]:


np.stack((studentId, name, scores), axis =1).shape


# ### 3. vstack
# Stacks row wise

# In[13]:


np.vstack((studentId, name, scores)) 


# ### 4. hstack
# Stacks column wise

# In[14]:


np.hstack((studentId, name, scores)) 


# In[84]:


np.hstack((studentId, name, scores)).shape


# The functions concatenate, stack and block provide more general stacking and concatenation operations.

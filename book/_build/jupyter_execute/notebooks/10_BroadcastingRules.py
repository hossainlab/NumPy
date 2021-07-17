#!/usr/bin/env python
# coding: utf-8

# ## Broadcasting

# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. 

# Broadcasting solves the problem of arithmetic between arrays of differing shapes by in effect replicating the smaller array along the last mismatched dimension.

# In[1]:


import numpy as np


# NumPy operations are usually done on pairs of arrays on an element-by-element basis. In the simplest case, the two arrays must have exactly the same shape, as in the following example:

# In[2]:


a = np.array([1,2,3,4,5])
b = np.array([10,10,10,10,10])


# In[3]:


a * b


# If the dimensions of two arrays are dissimilar, element-to-element operations are not possible. However, operations on arrays of non-similar shapes is still possible in NumPy, because of the <b>broadcasting </b> capability. The smaller array is broadcast to the size of the larger array so that they have compatible shapes.

# ### Scalar and One-Dimensional Array
# 

# A single value or scalar can be used in arithmetic with a one-dimensional array.

# In[4]:


c = 10


# In[5]:


a * c


# The result is equivalent to the previous example where b was an array. We can think of the scalar c being stretched during the arithmetic operation into an array with the same shape as a. The new elements in c are simply copies of the original scalar.

# ### Scalar and n-Dimensional Array

# A scalar value can be used in arithmetic with a n-dimensional array.

# In[6]:


one = np.ones((4,3))


# In[7]:


one * c


# ### One-Dimensional and n-Dimensional Arrays

# A one-dimensional array can be used in arithmetic with a n-dimensional array.

# Consider the following example: We have the heights (in cm) and weights ( in pounds) of a group of students. We store this information in an array called student_bio.
# * Heights are in cm
# * Weights are in kgs

# In[10]:


heights  = [165,170,168,183,172,169]
weights  = [61,76,56,81,62,60]


# In[11]:


student_bio = np.array([heights,weights])


# In[12]:


student_bio


# Now, we would like to convert heights into feet and weights into kilograms, for that the conversion factors are 0.0328084 and 2.20462 respectively

# In[13]:


factor_1 = np.array([0.0328084,2.20462 ])


# In[14]:


factor_1


# In[26]:


factor_1.shape


# In[27]:


student_bio.shape


# ### General Broadcasting Rules
# When operating on two arrays, NumPy compares their shapes element-wise. The dimensions are considered in reverse order, starting with the trailing dimensions, and working its way forward. Two dimensions are compatible when
# 
# 1) they are equal, <br />
# 2) one of them is of size 1

# #### Shape mismatch
# This fails because there is a mismatch in the trailing dimensions <br />
# student bio:  2 x <b>6</b> <br />
# factor_1:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       <b>2</b>
# 
# The trailing dimensions here are 6 and 2, so there is a mismatch

# In[15]:


student_bio * factor_1


# In[19]:


factor_2 = np.array([[0.0328084],[2.20462 ]])


# In[20]:


factor_2


# In[25]:


factor_2.shape


# #### Dimensions match
# The dimensions are: <br />
# 2 x 6 <br />
# 2 x 1 <br />
# 
# Here, the last dimensions are 6,1 so they match on account of one of them being 1 <br />
# The next dimensions are 2,2 so there is a match

# In[21]:


student_bio * factor_2


# <b>Why did we encounter an error for the first try? </b> 

# Broadcasting is possible only when certain rules are satisfied, it does not work for all cases, and imposes a strict rule that must be satisfied for broadcasting to be performed.

# The dimensions with size 1 are stretched or “copied” to match the other.
# 
# After application of the broadcasting rules, the sizes of all arrays must match.

# In the above example, factor is stretched to match  with the dimensions of students_bio in order to carry out operations.

#!/usr/bin/env python
# coding: utf-8

# ## Universal Functions

# NumPy provides standard trigonometric functions, functions for arithmetic operations, handling complex numbers, statistical functions,etc. In NumPy, these are called “universal functions”(ufunc).

# In[1]:


import numpy as np


# ### Trigonometric Functions

# In[14]:


angles = np.array([0,30,45,60,90]) 


# #### Angles need to be converted to radians by multiplying by pi/180 
# Only then can we appy trigonometric functions to our array

# In[15]:


angles_radians = angles * np.pi/180
angles_radians


# In[16]:


print('Sine of angles in the array:')
print(np.sin(angles_radians))      


# #### Alternatively, use the np.radians() function to convert to radians

# In[17]:


angles_radians = np.radians(angles)
angles_radians


# In[18]:


print('Cosine of angles in the array:')
print(np.cos(angles_radians))


# In[19]:


print('Tangent of angles in the array:')
print(np.tan(angles_radians))


# <b>arcsin</b>, <b>arcos</b>, and <b>arctan</b> functions return the trigonometric inverse of sin, cos, and tan of the given angle. The result of these functions can be verified by numpy.degrees() function by converting radians to degrees.

# In[20]:


sin = np.sin(angles * np.pi/180) 
print ('Compute sine inverse of angles. Returned values are in radians.')

inv = np.arcsin(sin) 
print (inv) 


# #### np.degrees() converts radians to degrees

# In[21]:


print ('Check result by converting to degrees:' )
print (np.degrees(inv)) 


# ### Statistical Functions

# In[22]:


test_scores = np.array([32.32, 56.98, 21.52, 44.32, 
                        55.63, 13.75, 43.47, 43.34])


# In[23]:


print('Mean test scores of the students: ')
print(np.mean(test_scores))


# In[24]:


print('Median test scores of the students: ')
print(np.median(test_scores))


# We will now perform basic statistical methods on real life dataset. We will use salary data of 1147 European developers.

# In[26]:


salaries = np.genfromtxt('data/salary.csv', 
                         delimiter=',')


# In[30]:


salaries


# In[31]:


salaries.shape


# In[27]:


mean     = np.mean(salaries)
median   = np.median(salaries)
sd       = np.std(salaries)
variance = np.var(salaries)


# In[28]:


print('Mean = %i' %mean)
print('Median = %i' %median)
print('Standard Deviation = %i' %sd)
print('Variance = %i' %variance)


#!/usr/bin/env python
# coding: utf-8

# # Getting Started
# Use the following import convention
# ```python
# import numpy as np
# ```

# ## Calculation
# - Element wise sum is not possible in Python list. But numpy can do that it is an advantage of numpy array
# 

# In[ ]:


# add 2 lists 
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1+L2)


# In[ ]:


# element wise sum using numpy array 
import numpy as np 
A1 = np.array([1, 2, 3])
A2 = np.array([4, 5, 6])
print(A1+A2)


# ## Less Memory

# In[ ]:


import numpy as np
import time
import sys
S = range(1000)
print("Python List: ", sys.getsizeof(5)*len(S))
 
D = np.arange(1000)
print("Numpy Array: ", D.size*D.itemsize)


# ## Faster

# In[ ]:


import time
import sys
 
SIZE = 1000000
 
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)
 
start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
# time in ms 
print((time.time()-start)*1000)
 
start = time.time()
result = A1+A2
# time in ms 
print((time.time()-start)*1000)


# In[ ]:


get_ipython().run_line_magic('timeit', 'sum(range(1000))')


# In[ ]:


get_ipython().run_line_magic('timeit', 'np.sum(np.arange(1000))')


# ## Creating Arrays 
# - **Array:** Ordered collection of elements of basic data types of given length.
# - **Syntax**
# ```python 
# np.array(object)
# ```

# In[ ]:


# import numpy 
import numpy as np 


# ### 1D Array

# In[ ]:


# Creating 1D array
A = np.array([1, 2, 3])
A 


# ### 2D Array

# In[ ]:


# Creating 2D array
B = np.array([[1, 2, 3], [3, 4, 5]])
B 


# ### 3D Array

# In[ ]:


# Creating 3D array
C = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
C 


# ## Printing Arrays
# When you print an array, NumPy displays it in a similar way to nested lists, One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.

# In[ ]:


# Printing arrays 
X = np.array([1, 2, 3, 4, 5])
print(X)


# If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners

# In[ ]:


# Prinitng large array 
print(np.arange(10000))


# In[ ]:


# Set threshold
np.set_printoptions(threshold = 2**32)


# In[ ]:


# Printing large arrays 
print(np.arange(10000)) 


# In[ ]:


# type 
print(type(A))


# ## Array with Categorical Entities 
# - Numpy can handle different categorical entities. 
# - All elements are coerced into same data type 

# In[ ]:


# create an array with categorical entities. 
X = np.array([12, 13, "n"])
print(X)


# In[ ]:


# type 
print(type(X))


# In[ ]:


# Creating 2D array
A2 = np.array([[3, 4, 5], [7, 8, 9]])
print(A2) 


# In[ ]:


# Creating 3D array
A3 = np.array([[(1, 2, 3), (4, 5, 6)], [(7, 8, 9), (10, 11, 12)]])
print(A3) 


# ## Inspecting array properties

# ### Size 
# - Returns number of elements in array
# - **Syntax:** `array.size`

# In[ ]:


A1 = np.array([1, 2, 3,4, 5])
# size 
A1.size


# ### Shape
# - Returns dimensions of array (rows,columns)
# - **Syntax:** `array.shape`

# In[ ]:


A2 = np.array([[4, 5, 6], [7, 8, 9]])
# shape 
A2.shape 


# In[ ]:


# get row 
A2.shape[0]


# In[ ]:


# get column
A2.shape[1]


# ### Data Type
# - Returns type of elements in array
# - **Syntax:** `array.dtype`

# In[ ]:


A3 = np.linspace(0, 100, 6)
# dtypes 
A3.dtype


# ## Type Conversion 
#  - Convert array elements to type dtype
#  - **Syntax:** `array.astype(dtype)`
#      - dtype - data type 

# In[ ]:


A4 = np.ones((2,3))
# convert 
A4.astype(np.float16)


# ## Numpy array to Python List 
# - Returns the Python list 
# - **Syntax:** `array.tolist()`

# In[ ]:


A5 = np.linspace(0, 100, 20)
# array to list 
A5.tolist() 


# ## Get Help: View documentation
# - Returns a documentation
# - **Syntax:** `np.info(np.function)`
#     - function - linspace, logspace, eye, ones, zeros etc.

# In[ ]:


np.info(np.linspace)


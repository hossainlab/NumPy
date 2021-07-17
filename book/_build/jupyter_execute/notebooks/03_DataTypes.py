#!/usr/bin/env python
# coding: utf-8

# # NumPy Data Types

# ## Data Types in Python 
# - `strings` - used to represent text data, the text is given under quote marks. eg. "ABCD"
# - `integer` - used to represent integer numbers. eg. -1, -2, -3
# - `float` - used to represent real numbers. eg. 1.2, 42.42
# - `boolean` - used to represent True or False.
# - `complex` - used to represent a number in complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j

# ## Data Types in NumPy 
# - `i` - integer
# - `b` - boolean
# - `u` - unsigned integer
# - `f` - float
# - `c` - complex float
# - `m` - timedelta
# - `M` - datetime
# - `O` - object
# - `S` - string
# - `U` - unicode string
# - `V` - fixed chunk of memory for other type ( void )

# ## Brief Overview of NumPy Data Types 

# |Data Type| Description|
# |---------|------------|
# |bool_ 	|Boolean (True or False) stored as a byte|
# |int_ 	|Default integer type (same as C long; normally either int64 or int32)|
# |intc 	|Identical to C int (normally int32 or int64)|
# |intp 	|Integer used for indexing (same as C ssize_t; normally either int32 or int64)|
# |int8 	|Byte (-128 to 127)|
# |int16 	|Integer (-32768 to 32767)|
# |int32  |Integer (-2147483648 to 2147483647)|
# |int64 	|Integer (-9223372036854775808 to 9223372036854775807)|
# |uint8 	|Unsigned integer (0 to 255)|
# |uint16 |Unsigned integer (0 to 65535)|
# |uint32 |Unsigned integer (0 to 4294967295)|
# |uint64 |Unsigned integer (0 to 18446744073709551615)|
# |float_ |Shorthand for float64|
# |float16|Half precision float: sign bit, 5 bits exponent, 10 bits mantissa|
# |float32 	|Single precision float: sign bit, 8 bits exponent, 23 bits mantissa|
# |float64 	|Double precision float: sign bit, 11 bits exponent, 52 bits mantissa|
# |complex_ 	|Shorthand for complex128.|
# |complex64 |	Complex number, represented by two 32-bit floats|
# |complex128 	|Complex number, represented by two 64-bit floats|

# ## Creating NumPy Array 

# In[1]:


import numpy as np 


# In[2]:


# Create a numpy array 
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(A)


# In[3]:


# Create a numpy array with strings 
S = np.array(["Jim", "Tim", "Mim"])
print(S)


# ## Checking the Data Type of an Array
# The NumPy array object has a property called `dtype` that returns the data type of the array:

# In[4]:


# Check the data type of `A`
A.dtype


# In[5]:


# Check rthe data type of `S`
S.dtype


# ## Creating Arrays With a Defined Data Type
# We use the `array()` function to create arrays, this function can take an optional argument: `dtype` that allows us to define the expected data type of the array elements

# In[6]:


# Create an array of integers 
B = np.array([1, 2, 3, 4, 5], dtype='int')
print(B)


# In[7]:


# Check data type of `B`
B.dtype


# In[8]:


# Create an array of floats 
C = np.array([1, 2, 3, 4, 5], dtype='float32')
print(C)


# In[9]:


# Check the data type of `C`
C.dtype


# ## Find Byte Size of an Array 

# In[10]:


# Check byte size of `A`
A.nbytes


# In[11]:


# Check byte size of `S`
S.nbytes


# In[12]:


# Check byte size of `B`
B.nbytes


# In[13]:


# Check byte size of `C`
C.nbytes


# ## Converting Data Type on Existing Arrays using  `astype()`

# In[14]:


# Create an array of floats 
arr = np.array([1, 2, 3, 4, 5], dtype='float32')
print(arr)


# In[15]:


# Convert the array into integer using astype()
new_arr = arr.astype('int')
print(new_arr)


# In[16]:


# Now check the data type again 
new_arr.dtype


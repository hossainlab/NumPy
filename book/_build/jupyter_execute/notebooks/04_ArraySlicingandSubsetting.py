#!/usr/bin/env python
# coding: utf-8

# # Array Indexing and Slicing 

# ## Array Indexing 
# This also follows zero based indexing like python lists

# In[ ]:


import numpy as np 


# ### 1D Array Indexing 
# One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences. The <b>(start:stop:step)</b> notation for slicing is used. 
# 
# - 1D array at index `i`
# - Returns the `ith` element of an array
# - **Syntax:** `array[i]`

# In[ ]:


# Create an 1D arary 
A1 = np.array([11, 22, 34, 12, 15])


# In[ ]:


# Select ith element of A1 
A1[1]


# In[ ]:


# Negative indexing 
A1[-1]


# ### 2D Array Indexing 
# - 2D array at index `[i][j]`
# - Returns the `[i][j]` element of an array
# - **Syntax:** `array[i][j]`

# In[ ]:


# Create an 2D array 
A2 = np.array([[0, 1, 3], [4, 6, 7]])


# In[ ]:


# Select the first row of A2 
A2[0]


# In[ ]:


# Select the first element of first row 
A2[0][0]


# __Note__
# 
# - First, `A2[0]` = [0, 1, 3], which is the first row of array `A2`
# - Second, `A2[0]` select the first element of first row. 

# In[ ]:


# Select the second row of A2 
A2[1]


# In[ ]:


# Select the 3rd element of second row 
A2[1][2]


# Consider an array students, it contains the test scores in two courses of the students against their names

# In[ ]:


students = np.array([['Alice','Beth','Cathy','Dorothy'],
                     [65,78,90,81],
                     [71,82,79,92]])


# In[ ]:


students


# In[ ]:


students[0]


# In[ ]:


students[1]


# In[ ]:


students[2]


# In[ ]:


students[0,1]


# ## Array Slicing

# ### 1D Array Slicing 

# In[ ]:


# Create a 1D Array 
A = np.array([11, 12, 13, 14, 15])


# In[ ]:


# Select all elements 
A[:]


# In[ ]:


# Returns n-1 
A[1:2]


# In[ ]:


# Select all except last element 
A[:-1]


# ### 2D Array slicing
# This will consider the rows 0 and 1, columns 2 and 3

# In[ ]:


# Create a 2D array of students info 
students = np.array([['Alice','Beth','Cathy','Dorothy'],
                     [65,78,90,81],
                     [71,82,79,92]])


# In[ ]:


# All rows and column 1
students[:,1:2]


# In[ ]:


# All rows, columns 1 and 2
students[:,1:3]


# In[ ]:


# All columns, rows 0 and 1
students[0:2,:]


# In[ ]:


# All rows and columns
students[:]


# In[ ]:


# The last row
students[-1,:]


# In[ ]:


# 3rd from last to second from last row, last two columns
students[-3:-1,-2:]


# ### Dots or ellipsis(...)

# Slicing can also include ellipsis (…) to make a selection tuple of the same length as the dimension of an array. The dots (...) represent as many colons as needed to produce a complete indexing tuple

# ##### Equivalent to students[0] or students[0:1,:]
# Select row 0 and all columns

# In[ ]:


students[0,...] 


# In[ ]:


# All rows and column 1 
students[...,1]


# In[ ]:


students[...,1].shape


# In[ ]:


students[:,1:2].shape


# ## Fancy Indexing - Integer Arrays

# NumPy arrays can be indexed with slices, but also with boolean or integer arrays <b>(masks)</b>. It means passing an array of indices to access multiple array elements at once. This method is called fancy indexing. It creates copies not views.

# In[ ]:


a = np.arange(12)**2   


# In[ ]:


a


# Suppose we want to access three different elements. We could do it like this:

# In[ ]:


a[2],a[6],a[8]


# Alternatively, we can pass a single list or array of indices to obtain the same result:

# In[ ]:


indx_1 = [2,6,8]


# In[ ]:


a[indx_1]


# When using fancy indexing, the shape of the result reflects the shape of the index arrays rather than the shape of the array being indexed

# In[ ]:


indx_2 = np.array([[2,4],[8,10]])


# In[ ]:


indx_2


# In[ ]:


a[indx_2]


# We can also give indexes for more than one dimension. The arrays of indices for each dimension must have the same shape.

# In[ ]:


food = np.array([["blueberry","strawberry","cherry","blackberry"],
                 ["pinenut","hazelnuts","cashewnut","coconut"],
                 ["mustard","paprika","nutmeg","clove"]])


# In[ ]:


food


# ##### We will now select the corner elements of this array

# In[ ]:


row = np.array([[0,0],[2,2]])
col = np.array([[0,3],[0,3]])


# In[ ]:


food[row,col]


# Notice that the first value in the result is food[0,0], next is food[0,3] , food[2,0] and lastly food[2,3]

# In[ ]:


food[2,0]


# ### Modifying Values with Fancy Indexing

# Just as fancy indexing can be used to access parts of an array, it can also be used to modify parts of an array.

# In[ ]:


food[row,col] = "000000"


# In[ ]:


food


# We can use any assignment-type operator for this. Consider following example:

# In[ ]:


a


# In[ ]:


indx_1


# In[ ]:


a[indx_1] = 999


# In[ ]:


a


# In[ ]:


a[indx_1] -=100


# In[ ]:


a


# ## Fancy Indexing - Boolean Arrays

# When we index arrays with arrays of (integer) indices we are providing the list of indices to pick. With boolean indices the approach is different; we explicitly choose which items in the array we want and which ones we don’t.

# Frequently this type of indexing is used to select the elements of an array that satisfy some condition

# In[ ]:


a = np.arange(16).reshape(4,4)


# In[ ]:


a


# Now we find the elements that are greater than 9. This will return a numpy array of the same shape as our original array. 

# In[ ]:


indx_bool = a > 9


# In[ ]:


indx_bool


# We use this array to select elements in a corresponding to 'true' values in the boolean array.

# In[ ]:


a[indx_boo]


# We can do all of the above in a single concise statement

# In[ ]:


print(a[a > 9])


# ### Counting 

# #### How many values less than 6?

# In[ ]:


a < 6


# In[ ]:


np.count_nonzero(a < 6)


# In[ ]:


np.sum(a < 6)


# #### How many values less than 6 in each row?

# In[ ]:


np.sum(a < 6, axis=1)


# #### Are there any values greater than 8?

# In[ ]:


np.any(a > 8)


# #### Are all values less than 10?

# In[ ]:


np.all(a < 10)


# #### Are all values less than 100?

# In[ ]:


np.all(a < 100)


# #### Are all values in each row less than 9?

# In[ ]:


np.all(a < 9, axis=1)


# ## Structured Arrays

# <b>Structured arrays</b> or <b>record arrays</b> are useful when you perform computations, and at the same time you could keep closely related data together. Structured arrays provide efficient storage for compound, heterogeneous data.

# NumPy also provides powerful capabilities to create arrays of records, as multiple data types live in one NumPy array. However, one principle in NumPy that still needs to be honored is that the data type in each field (think of this as a column in the records) needs to be homogeneous. 

# Imagine that we have several categories of data on a number of students say, name, roll number, and test scores.

# In[ ]:


name  = ["Alice","Beth","Cathy","Dorothy"]
studentId  = [1,2,3,4]
score = [85.4,90.4,87.66,78.9]


# There's nothing here that tells us that the three arrays are related; it would be more natural if we could use a single structure to store all of this data. 

# ##### Define the np array with the names of the 'columns' and the data format for each
# * U10 represents a 10-character Unicode string
# * i4 is short for int32 (i for int, 4 for 4 bytes)
# * f8 is shorthand for float64

# In[ ]:


student_data = np.zeros(4, dtype={'names':('name', 'studentId', 'score'),
                          'formats':('U10', 'i4', 'f8')})


# #### np.zeros() for a string sets it to an empty string

# In[ ]:


student_data


# In[ ]:


print(student_data.dtype)


# Now that we've created an empty container array, we can fill the array with our lists of values

# In[ ]:


student_data['name'] = name
student_data['studentId'] = studentId
student_data['score'] = score


# In[ ]:


print(student_data)


# The handy thing with structured arrays is that you can now refer to values either by index or by name

# In[ ]:


student_data['name']


# In[ ]:


student_data['studentId']


# In[ ]:


student_data['score']


# If you index student_data at position 1 you get a structure:

# In[ ]:


student_data[1]


# ##### Get the name attribute from the last row

# In[ ]:


student_data[-1]['name']


# ##### Get names where score is above 85

# In[ ]:


student_data[student_data['score'] > 85]['name']


# Note that if you'd like to do any operations that are any more complicated than these, you should probably consider the Pandas package with provides a powerful data structure called data frames.

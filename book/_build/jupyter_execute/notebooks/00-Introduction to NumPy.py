# Introduction to NumPy

## What is NumPy?

NumPy is a Python package which stands for ‘Numerical Python’. It is the core library for scientific computing, which contains a powerful n-dimensional array object, provide tools for integrating C, C++ etc. It is also useful in linear algebra, random number capability etc. NumPy array can also be used as an efficient multi-dimensional container for generic data. Now, let me tell you what exactly is a python numpy array.

## Keypoints 
- Numpy stands for numerical Python
- Fundamental package for numerical computations in Python
- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

## NumPy Array
Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize numpy arrays from nested Python lists and access it elements. In order to perform these numpy operations.

## N-dimensional Array
- 1Dimensional(1D) Array
- 2Dimensional(2D) Array
- 3Dimensional(3D) Array
![NdArray](../img/arrays.png)

## Getting Started
Use the following import convention
```python
import numpy as np
```

## Why Numpy?
- Less Memory
- Fast
- Convenient

## Calculation
- Element wise sum is not possible in Python list. But numpy can do that it is an advantage of numpy array


# add 2 lists 
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1+L2)

# element wise sum using numpy array 
import numpy as np 
A1 = np.array([1, 2, 3])
A2 = np.array([4, 5, 6])
print(A1+A2)

## Less Memory

import numpy as np
import time
import sys
S = range(1000)
print("Python List: ", sys.getsizeof(5)*len(S))
 
D = np.arange(1000)
print("Numpy Array: ", D.size*D.itemsize)

## Faster

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

%timeit sum(range(1000))

%timeit np.sum(np.arange(1000))

## Creating Arrays 
- **Array:** Ordered collection of elements of basic data types of given length.
- **Syntax**
```python 
np.array(object)
```

# import numpy 
import numpy as np 

# Creating 1D array
A = np.array([1, 2, 3])
print(A)

# type 
print(type(A))

## Array with Categorical Entities 
- Numpy can handle different categorical entities. 
- All elements are coerced into same data type 

# create an array with categorical entities. 
X = np.array([12, 13, "n"])
print(X)

# type 
print(type(X))

# Creating 2D array
A2 = np.array([[3, 4, 5], [7, 8, 9]])
print(A2) 

# Creating 3D array
A3 = np.array([[(1, 2, 3), (4, 5, 6)], [(7, 8, 9), (10, 11, 12)]])
print(A3) 

## Inspecting array properties

### Size 
- Returns number of elements in array
- **Syntax:** `array.size`

A1 = np.array([1, 2, 3,4, 5])
# size 
A1.size

### Shape
- Returns dimensions of array (rows,columns)
- **Syntax:** `array.shape`

A2 = np.array([[4, 5, 6], [7, 8, 9]])
# shape 
A2.shape 

# get row 
A2.shape[0]

# get column
A2.shape[1]

### Data Type
- Returns type of elements in array
- **Syntax:** `array.size`

A3 = np.linspace(0, 100, 6)
# dtypes 
A3.dtype

 ## Type Conversion 
 - Convert array elements to type dtype
 - **Syntax:** `array.astype(dtype)`
     - dtype - data type 

A4 = np.ones((2,3))
# convert 
A4.astype(np.float16)

## Numpy array to Python List 
- Returns the Python list 
- **Syntax:** `array.tolist()`

A5 = np.linspace(0, 100, 20)
# array to list 
A5.tolist() 

## Get Help: View documentation
- Returns a documentation
- **Syntax:** `np.info(np.function)`
    - function - linspace, logspace, eye, ones, zeros etc.

np.info(np.linspace)
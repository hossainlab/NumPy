<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-to-NumPy" data-toc-modified-id="Introduction-to-NumPy-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to NumPy</a></span><ul class="toc-item"><li><span><a href="#What-is-NumPy?" data-toc-modified-id="What-is-NumPy?-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What is NumPy?</a></span></li><li><span><a href="#Keypoints" data-toc-modified-id="Keypoints-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Keypoints</a></span></li><li><span><a href="#NumPy-Array" data-toc-modified-id="NumPy-Array-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>NumPy Array</a></span></li><li><span><a href="#N-dimensional-Array" data-toc-modified-id="N-dimensional-Array-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>N-dimensional Array</a></span></li><li><span><a href="#Getting-Started" data-toc-modified-id="Getting-Started-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Getting Started</a></span></li><li><span><a href="#Why-Numpy?" data-toc-modified-id="Why-Numpy?-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Why Numpy?</a></span></li><li><span><a href="#Calculation" data-toc-modified-id="Calculation-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Calculation</a></span></li><li><span><a href="#Less-Memory" data-toc-modified-id="Less-Memory-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Less Memory</a></span></li><li><span><a href="#Faster" data-toc-modified-id="Faster-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Faster</a></span></li><li><span><a href="#Creating-Arrays" data-toc-modified-id="Creating-Arrays-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Creating Arrays</a></span></li><li><span><a href="#Array-with-Categorical-Entities" data-toc-modified-id="Array-with-Categorical-Entities-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Array with Categorical Entities</a></span></li><li><span><a href="#Inspecting-array-properties" data-toc-modified-id="Inspecting-array-properties-1.12"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>Inspecting array properties</a></span><ul class="toc-item"><li><span><a href="#Size" data-toc-modified-id="Size-1.12.1"><span class="toc-item-num">1.12.1&nbsp;&nbsp;</span>Size</a></span></li><li><span><a href="#Shape" data-toc-modified-id="Shape-1.12.2"><span class="toc-item-num">1.12.2&nbsp;&nbsp;</span>Shape</a></span></li><li><span><a href="#Data-Type" data-toc-modified-id="Data-Type-1.12.3"><span class="toc-item-num">1.12.3&nbsp;&nbsp;</span>Data Type</a></span></li></ul></li><li><span><a href="#Type-Conversion" data-toc-modified-id="Type-Conversion-1.13"><span class="toc-item-num">1.13&nbsp;&nbsp;</span>Type Conversion</a></span></li><li><span><a href="#Numpy-array-to-Python-List" data-toc-modified-id="Numpy-array-to-Python-List-1.14"><span class="toc-item-num">1.14&nbsp;&nbsp;</span>Numpy array to Python List</a></span></li><li><span><a href="#Get-Help:-View-documentation" data-toc-modified-id="Get-Help:-View-documentation-1.15"><span class="toc-item-num">1.15&nbsp;&nbsp;</span>Get Help: View documentation</a></span></li><li><span><a href="#References" data-toc-modified-id="References-1.16"><span class="toc-item-num">1.16&nbsp;&nbsp;</span>References</a></span></li></ul></li></ul></div>

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

## References
- https://numpy.org/
- https://www.edureka.co/blog/python-numpy-tutorial/
- https://github.com/enthought/Numpy-Tutorial-SciPyConf-2019
- [Python Machine Learning Cookbook](https://www.amazon.com/Python-Machine-Learning-Cookbook-Prateek/dp/1786464470)
<hr>

*This notebook was created by [Jubayer Hossain](https://jhossain.me/) | Copyright &copy; 2020, [Jubayer Hossain](https://jhossain.me/)*
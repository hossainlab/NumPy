<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Copying,-Sorting-and-Reshaping" data-toc-modified-id="Copying,-Sorting-and-Reshaping-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Copying, Sorting and Reshaping</a></span><ul class="toc-item"><li><span><a href="#Copy" data-toc-modified-id="Copy-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Copy</a></span></li><li><span><a href="#View" data-toc-modified-id="View-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>View</a></span></li><li><span><a href="#Sorting" data-toc-modified-id="Sorting-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Sorting</a></span></li><li><span><a href="#Flatten:-Flattens-2D-array-to-1D-array" data-toc-modified-id="Flatten:-Flattens-2D-array-to-1D-array-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Flatten: Flattens 2D array to 1D array</a></span></li><li><span><a href="#Transpose:-Transposes-array-(rows-become-columns-and-vice-versa)" data-toc-modified-id="Transpose:-Transposes-array-(rows-become-columns-and-vice-versa)-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Transpose: Transposes array (rows become columns and vice versa)</a></span></li><li><span><a href="#Reshape:-Reshapes-arr-to-r-rows,-c-columns-without-changing-data" data-toc-modified-id="Reshape:-Reshapes-arr-to-r-rows,-c-columns-without-changing-data-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Reshape: Reshapes arr to <code>r</code> rows, <code>c</code> columns without changing data</a></span></li><li><span><a href="#Resize:--Changes-arr-shape-to-rxc-and-fills-new-values-with-0" data-toc-modified-id="Resize:--Changes-arr-shape-to-rxc-and-fills-new-values-with-0-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Resize:  Changes arr shape to <code>rxc</code> and fills new values with 0</a></span></li><li><span><a href="#References" data-toc-modified-id="References-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>References</a></span></li></ul></li></ul></div>

# Copying, Sorting and Reshaping

# import numpy 
import numpy as np

## Copy
- Copies array to new memory
- **Syntax:** `np.copy(array)`

# create an array `A1`
A1 = np.arange(10)
print(A1)

# copy `A1` into A2 
A2 = np.copy(A1)
print(A2)

## View
- Creates view of array elements with type(dtype)
- **Syntax:** `array.view(np.dtype)`

# view of array A2 
A3 = A2.view(np.float16)
print(A3)

## Sorting
- Returns a sorted copy of an array.
- **Syntax:** `array.sort()`
    - element-wise sorting(default) 
    - axis = 0; row
    - axis = 1; column
![Axis](../img/axis.png)

# Unsorted array
A4 = np.array([9, 2, 3,1, 5, 10])
print(A4) 

# Call sort function
A4.sort()
print(A4)

# Row and column unsorted
A5 = np.array([[4, 1, 3], [9, 5, 8]])
print(A5) 

# Apply sort function on column axis=1
A5.sort(axis=1)
print(A5)

## Flatten: Flattens 2D array to 1D array


# 2D array
A6 = np.array([[4, 1, 3], [9, 5, 8]])
# 1D array 
A6.flatten()

## Transpose: Transposes array (rows become columns and vice versa)


A7 = np.array([[4, 1, 3], [9, 5, 8]])
A7

# Transpose A7 
A7.T

## Reshape: Reshapes arr to `r` rows, `c` columns without changing data
![Reshape](../img/reshape.png)

A8 = np.array([(8,9,10),(11,12,13)])
A8

# Reshape --> 3x4
A8.reshape(3,2)

## Resize:  Changes arr shape to `rxc` and fills new values with 0


A9 = np.array([(8,9,10),(11,12,13)])
A9

# Resize 
A9.resize(3, 2)
A9

## References
- https://numpy.org/
- https://www.edureka.co/blog/python-numpy-tutorial/
- https://github.com/enthought/Numpy-Tutorial-SciPyConf-2019
- [Python Machine Learning Cookbook](https://www.amazon.com/Python-Machine-Learning-Cookbook-Prateek/dp/1786464470)
<hr>

*This notebook was created by [Jubayer Hossain](https://jhossain.me/) | Copyright &copy; 2020, [Jubayer Hossain](https://jhossain.me/)*
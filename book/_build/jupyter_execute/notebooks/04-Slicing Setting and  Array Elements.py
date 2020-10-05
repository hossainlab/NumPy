# Setting and Slicing Array Elements

import numpy as np 

## Array Slicing

# Create an array 
A = np.array([0, 1, 2, 3])
print(A)

### Positive Indexing
Select `nth` element of an array by using `var[position]`

# Select 0th element of `A`
A[0]

# Select 1st element of `A`
A[1]

### Negative Indexing

# Select last element of `A`
A[-1]

A[-2]

Extract a Portion of a Sequence by specifying a lower and upper bound. The lower bound element is `included`, but the upper-bound element is `not included`. Mathematically: [lower, upper]. The stop value specifies the stride between elements.


B = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# indices
B[1:3]

# negative indices work also
B[1:-2]

B[-4:3]

Omitted boundaries are assumed to be the beginning (or end) of the list

# grab first theree elements 
B[:3]

# grab last two elements 
B[-2:]

# grab every other elements 
B[::2]

## 2D Array Slicing

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# grab 1st row and 1st element 
arr[0, 0]

# same as above
arr[0, 2]

# negative indexing 
arr[0, -1]

# select all rows and last element
arr[:, 2]
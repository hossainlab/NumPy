# Array Creation Function

# import numpy 
import numpy as np 

## Generate arrays using `zeros()`
- Returns an array of given shape and type filled with zeros 
- **Syntax:** `np.zeros(shape, dtype)`
    - shape - integer or sequence of integers
    - dtype - data type(default: float)

# 1D array of length 3 with all values 0 
Z1 = np.zeros(3)
print(Z1)

# 2D array of 3x4 with all values 0 
Z2 = np.zeros((3,4))
print(Z2)

## Generate arrays using `ones()`
- Returns an array of given shape and type filled with ones 
- **Syntax:** `np.ones(shape, dtype)`
    - shape - integer or sequence of integers 
    - dtype - data type(default: float) 

# 1D array of length 3 with all values 1
A1 = np.ones(3)  
print(A1) 

__Note__
- Rows = 3 
- Columns = 4 

# 2D array of 3x4 with all values 1
A2 = np.ones((3,4))
A2
print(A2) 

## Generate arrays using `arange()`
- Returns equally spaced numbers with in the given range based on step size. 
- **Syntax:** `np.arange(start, stop, step)`
    - start- starts of interval range 
    - stop - end of interval range '
    - step - step size of interval 

# not specify start and step 
A1 = np.arange(10)
print(A1)

# specifying start and step 
A2 = np.arange(start=1, stop=10, step=2)
print(A2)

# another way 
A3 = np.arange(10, 25, 2)
print(A3)

## Generate arrays using `linspace()`
- Returns equally spaced numbers within the given range based on the sample number. 
- **Syntax:**  `np.linspace(start, stop, num, dtype, retstep)`
    - start-start of interval range 
    - stop-end of the interval range 
    - num- number of samples to be generated 
    - dtype-type of output array 
    - retstep-return the samples, step values 

# array of evenly spaced values 0 to 2, here sample size = 9
L1 = np.linspace(0,2,9)
print(L1)

# Array of 6 evenly divided values from 0 to 100
L2 = np.linspace(0, 100, 6)
print(L2) 

# Array of 1 to 5
L3 = np.linspace(start=1, stop=5, endpoint=True, retstep=False)
print(L3) 

# Array of 1 to 5
L4 = np.linspace(start=1, stop=5, endpoint=True, retstep=True)
print(L4) 

__Specifying Endpoint__
- `endpoint=True`, inlcude 5 
- `endpoint=False`,exclude 5 

__Specifying Retstep__
- `retstep=False`, doesn't return the step value
- `endpoint=False`, returns the samples as well step value 

## Generate arrays using `logspace()`
- Returns equally spaced numbers within the given range based on the log scale. 
- **Syntax:**  `np.logspace(start, stop, num, endpoint, base, dtype, retstep)`
    - start- start of the sequence 
    - stop- end of the sequence  
    - num- number of samples to be generated(default: 50)  
    - dtype- type of output array 
    - retstep- return the samples, step values 
    - endpoint - if true, stop is the last sample 
    - base - base of the log space(default: 10.0) 

# generate an array with 5 samples with base 10.0 
np.logspace(1, 10, num=5, endpoint=True)

# generate an array with 5 samples with base 2.0
np.logspace(1, 10, num=5, endpoint=True, base=2.0)

## Generate constant arrays using `full()` 
- Return a new array of given shape and type, filled with `fill_value`. 
- **Syntax:** `np.full(shape,fill_value, dtype)`
    - shape - Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    - fill_value - Fill value(scaler).
    - dtype - The desired data-type for the array

# generate 2x2 constant array, constant = 7
C = np.full((2, 2), 7)
print(C)

## Creating identity matrix using `eye()`
- An array where all elements are equal to zero, except for the `k`-th
  diagonal, whose values are equal to one
- **Syntax:** `np.eye(N, M, k, dtype)`
    - N : Number of rows(int) in the output
    - M : Number of columns in the output. If None, defaults to `N`.
    - k : Index of the diagonal: 0 (the default) refers to the main diagonal,
      a positive value refers to an upper diagonal, and a negative value
      to a lower diagonal
    - dtype: Data-type of the returned array.

# generate 2x2 identity matrix 
I = np.eye(2)
print(I) 

## Generate arrays using random.rand() 
- Returns an array of given shape filled with random values. 
- **Syntax:** `np.random.rand(shape)`
    - shape - integer or sequence of integer 

# create an array with randomly generated 5 values 
R = np.random.rand(5)
print(R)

# generate 2x2 array of random values 
R1 = np.random.random((2, 2))
print(R1)

# generate 4x5 array of random floats between 0-1
R2 = np.random.rand(4,5)
print(R2)

# generate 6x7 array of random floats between 0-100
R3 = np.random.rand(6,7)*100
print(R3)

# generate 2x3 array of random ints between 0-4
R4 = np.random.randint(5, size=(2,3))
print(R4)

## Generate empty arrays using `empty()`
- Return a new array of given shape and type, without initializing entries.
- **Syntax:** `np.empty(shape, dtype)`
    - shape - integer or tuple of integer
    - dtype - data-type


# generate an empty array 
E1 = np.empty(2) 
print(E1)

# 2x2 empty array
E2 = np.empty((2, 2)) 
print(E2)

## Arrays using specific data type 
- float16
- float32 
- int8

__SEE MORE__
- https://numpy.org/devdocs/user/basics.types.html

# generate an array of floats 
D = np.ones((2, 3, 4), dtype=np.float16)
D
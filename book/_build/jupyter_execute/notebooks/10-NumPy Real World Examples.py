# NumPy Real World Examples

\begin{exercise}
Write a NumPy program to get the numpy version and show numpy build configuration.
\end{exercise}

import numpy as np 

# NumPy Version 
np.__version__

# NumPy build config 
np.show_config() 

\begin{exercise}
Write a NumPy program to get help on the add function.
\end{exercise}


# get help from NumPy 
np.info(np.add)

\begin{exercise}
Write a NumPy program to test whether none of the elements of a given array is zero.
\end{exercise}

# Solution: if zero not exist 
A1 = np.array([2, 3, 4, 5 , 6]) 
np.all(A1)

# Solution: if zero exist in array 
A2 = np.array([0, 0, 2, 3, 4, 5 , 6]) 
np.all(A2)

\begin{exercise}
Write a NumPy program to test whether any of the elements of a given array is non-zero.
\end{exercise}

# Solution: if zero not exist 
X1 = np.array([2, 3, 4, 5 , 6]) 
np.any(X1)

# Solution: if zero exist in array 
X2 = np.array([0, 0, 0, 0, 0, 0]) 
np.all(X2)

np.info(np.any)

## References
- https://numpy.org/
- https://www.edureka.co/blog/python-numpy-tutorial/
- https://github.com/enthought/Numpy-Tutorial-SciPyConf-2019
- [Python Machine Learning Cookbook](https://www.amazon.com/Python-Machine-Learning-Cookbook-Prateek/dp/1786464470)
<hr>

*This notebook was created by [Jubayer Hossain](https://jhossain.me/) | Copyright &copy; 2020, [Jubayer Hossain](https://jhossain.me/)*
#!/usr/bin/env python
# coding: utf-8

# # Linear Algebra 

# ## What is Linear Algebra? 
# Linear algebra is the branch of mathematics concerning linear equations such as linear maps such as and their representations in vector spaces and through matrices. Linear algebra is central to almost all areas of mathematics [See More](https://en.wikipedia.org/wiki/Linear_algebra)
# 
# ## Applications of Linear Algebra in Data Science
# - Loss Functions
# - Regularization
# - Covariance Matrix
# - Support Vector Machine Classification
# - Principal Component Analysis (PCA)
# - Singular Value Decomposition
# - Word Embeddings
# - Latent Semantic Analysis (LSA)
# - Image Representation as Tensors
# - Convolution and Image Processing
# 
# __SEE DETAILS:__
# https://www.analyticsvidhya.com/blog/2019/07/10-applications-linear-algebra-data-science/

# ## Linear Algebra Operations 

# In[1]:


# import numpy
import numpy as np 


# ### Determinant of matrix 
# - The determinant of a matrix is a special number that can be calculated from a **square matrix**
# \begin{equation}
# A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \\ 
# det(A) = ad - bc 
# \end{equation}
# Whre, A is a $2 \times 2$ matrix. 
# 
# - `np.linalg.det()` - performs determinant of the matrix 
# - **Syntax:** `np.linalg.det(matrix)`
# 
# __Source:__
# https://www.mathsisfun.com/algebra/matrix-determinant.html

# In[2]:


A = np.arange(0, 16).reshape(4,4)
print(A)


# In[3]:


# determinant of A 
np.linalg.det(A) 


# In[4]:


B = np.matrix("4,5,6,7;2,-3,3,3; 3,4,5,6; 4, 7,8,9")


# In[5]:


# determinant of B 
np.linalg.det(B)


# ### Rank of matrix 
# - `np.linalg.matrix_rank()` - returns rank of the matrix 
# - **Syntax:** `np.linalg.matrix_rank(matrix)`

# In[6]:


# rank 
np.linalg.matrix_rank(A)


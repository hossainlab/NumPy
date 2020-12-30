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

# In[4]:


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

# In[17]:


# create matrix A
A = np.matrix("4, 5, 16, 7; 2,-3,2,3; 3,4,5,6; 4,7,8,9")
print(A)


# In[18]:


# create matrix B
B = np.matrix("4,5,6,7;2,-3,3,3; 3,4,5,6; 4, 7,8,9")
print(B)


# In[19]:


# determinant of A 
np.linalg.det(A) 


# In[20]:


# determinant of B 
np.linalg.det(B)


# ### Rank of matrix 
# - `np.linalg.matrix_rank()` - returns rank of the matrix 
# - **Syntax:** `np.linalg.matrix_rank(matrix)`

# In[21]:


# rank of matrix A 
np.linalg.matrix_rank(A)


# In[22]:


# rank of matrix B 
np.linalg.matrix_rank(B)


# ### Inverse of a Matrix 
# - `np.linalg.inv()` - returns the multiplicative inverse of a matrix.
# - **Syntax:** `np.linalg.inv(matrix)`

# In[23]:


# inverse of matrix A 
np.linalg.inv(A)


# In[24]:


# inverse of matrix B 
np.linalg.inv(B)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


### Rank of matrix 
- `np.linalg.matrix_rank()` - returns rank of the matrix 
- **Syntax:** `np.linalg.matrix_rank(matrix)`


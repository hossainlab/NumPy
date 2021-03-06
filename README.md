# Introduction to NumPy


### What is NumPy?

`NumPy` is a Python package which stands for ‘Numerical Python’. It is the core library for scientific computing, which contains a powerful n-dimensional array object, provide tools for integrating C, C++ etc. It is also useful in linear algebra, random number capability etc. NumPy array can also be used as an efficient multi-dimensional container for generic data. Now, let me tell you what exactly is a python numpy array.

### Keypoints
- Numpy stands for numerical Python
- Fundamental package for numerical computations in Python
- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

### NumPy Array
Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize numpy arrays from nested Python lists and access it elements. In order to perform these numpy operations.

### N-dimensional Array
- 1Dimensional(1D) Array
- 2Dimensional(2D) Array
- 3Dimensional(3D) Array

### How to create your own Jupyter Book

1. `conda env create -f environment.yml`
2. `conda activate dsn-template`

### Building a Jupyter Book

Run the following command in your terminal: `jb build book/`.
If you would like to work with a clean build, you can empty the build folder by running `jb clean book/`. If the jupyter execution is cached, this command will not delete the cached folder. To remove the build folder, you can run `jb clean --all book/`.

### Publishing this Jupyter Book

Run `ghp-import -n -p -f book/_build/html`

import numpy as np

# Compute outer product of vectors
v = np.array([1, 2, 3])  # v has shape (3,)
w = np.array([4, 5])    # w has shape (2,)
"""
To compute an outer product, we first reshape v to be a column
vector of shape (3, 1); we can then broadcast it against w to yield
an output of shape (3, 2), which is the outer product of v and w:
[[ 4  5]
 [ 8 10]
 [12 15]]
 """
print(np.reshape(v, (3, 1)) * w)

# Add a vector to each row of a matrix
x = np.array([[1, 2, 3], [4, 5, 6]])
"""
x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
giving the following matrix:
[[2 4 6]
 [5 7 9]]
 """
print(x + v)
"""
Add a vector to each column of a matrix
x has shape (2, 3) and w has shape (2,).
If we transpose x then it has shape (3, 2) and can be broadcast
against w to yield a result of shape (3, 2); transposing this result
yields the final result of shape (2, 3) which is the matrix x with
the vector w added to each column. Gives the following matrix:
[[ 5  6  7]
 [ 9 10 11]]
 """
print((x.T + w).T)
"""
Another solution is to reshape w to be a row vector of shape (2, 1);
we can then broadcast it directly against x to produce the same output.
"""
print(x + np.reshape(w, (2, 1)))
"""
Multiply a matrix by a constant:
x has shape (2, 3). Numpy treats scalars as arrays of shape ();
these can be broadcast together to shape (2, 3), producing the
following array:
[[ 2  4  6]
 [ 8 10 12]]
"""
print(x * 2)

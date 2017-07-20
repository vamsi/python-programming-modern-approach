import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x)
print(x.T)
# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1, 2, 3])
print(v)
print(v.T)
"""
Output
[[1 2]
 [3 4]]

[[1 3]
 [2 4]]

[1 2 3]

[1 2 3]
"""

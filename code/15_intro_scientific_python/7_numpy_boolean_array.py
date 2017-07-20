import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

bool_idx = (a > 2)
"""
Find the elements of a that are bigger than 2;
this returns a numpy array of Booleans of the same
shape as a, where each slot of bool_idx tells
whether that element of a is > 2.
"""
print(bool_idx)
"""
Prints "[[False False]
[ True  True]
[ True  True]]"

We use boolean array indexing to construct a rank 1 array
consisting of the elements of a corresponding to the True values
of bool_idx
"""
print(a[bool_idx])
# Prints "[3 4 5 6]"
# We can do all of the above in a single concise statement:
print(a[a > 2])
# Prints "[3 4 5 6]"

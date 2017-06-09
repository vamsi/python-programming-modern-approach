import numpy as np

# Create a new array from which we will select elements
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a)
"""
prints array([[ 1,  2,  3],
[ 4,  5,  6],
[ 7,  8,  9],
[10, 11, 12]])
"""

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])
# Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)
"""
prints array([[11,  2,  3],
[ 4,  5, 16],
[17,  8,  9],
[10, 21, 12]])
"""

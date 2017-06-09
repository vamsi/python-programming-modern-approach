import numpy as np
from scipy.spatial.distance import pdist, squareform

"""
 Create the following array where each row is a point in 2D space:
 [[0 1]
  [1 0]
  [2 0]]
"""
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

"""
Compute the Euclidean distance between all rows of x.
d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
and d is the following array:
[[ 0.          1.41421356  2.23606798]
 [ 1.41421356  0.          1.        ]
 [ 2.23606798  1.          0.        ]]
"""
d = squareform(pdist(x, 'euclidean'))


print(d)

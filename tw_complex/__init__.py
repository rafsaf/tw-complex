__version__ = "0.1.0"


# An example of assigning (mapping) elements of one set to points to the elements of another set of points, such that the sum Euclidean distance is minimized.

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

np.random.seed(100)
# print(np.random.rand(100, 2))
points1 = np.random.rand(200, 2) + 200
points2 = np.random.rand(50000, 2)
x1 = time.time()
C = cdist(points1, points2)
print(time.time() - x1)
# _, assigment = linear_sum_assignment(C)
#
# plt.plot(points1[:, 0], points1[:, 1], "bo", markersize=10)
# plt.plot(points2[:, 0], points2[:, 1], "rs", markersize=7)
# for p in range(100):
#    plt.plot(
#        [points1[p, 0], points2[assigment[p], 0]],
#        [points1[p, 1], points2[assigment[p], 1]],
#        "k",
#    )
#
# plt.show()
#

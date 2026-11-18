
import numpy as np

pixels = np.array([
    [20, 40, 60, 80, 100],
    [30, 50, 70, 90, 110],
    [40, 60, 80, 100, 120],
    [50, 70, 90, 110, 130],
    [60, 80, 100, 120, 140]
], dtype=np.uint8)

# Task 1: Print array properties
print("shape",pixels.shape) 
print("datatype",pixels.dtype)
print("dimensions",pixels.ndim)

# Task 2: Calculate statistics
print("mean",np.mean(pixels))
print("max",pixels.max())
print("min",pixels.min())
# Task 3: Extract center 3x3 array 
print(pixels[:3,:3])

# Task 4: Create a thresholded array
# > 100 becomes 255, otherwise 0
thresholded = np.where(pixels > 100, 255, 0)
print(thresholded)
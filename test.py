import sys
import os
print("Python search paths:", sys.path)
print("Current directory:", os.getcwd())

from douglas_peucker import douglas_peucker


# Test points
test_points = [(0, 0), (1, 0), (10, 1), (11, 1), (15, 2), (17, 1),
               (20, 1), (27, 0), (28, 4), (30, 6), (33, 8), (34, 0)]

# Test with different thresholds
for threshold in [0.5, 1, 2]:
    simplified_points = douglas_peucker(test_points, threshold)
    print(f"Threshold: {threshold}, Simplified Points: {simplified_points}")

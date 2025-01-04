import sys
import os
import matplotlib.pyplot as plt
from douglas_peucker import douglas_peucker

# Test points
test_points = [(0, 0), (1, 0), (10, 1), (11, 1), (15, 2), (17, 1),
               (20, 1), (27, 0), (28, 4), (30, 6), (33, 8), (34, 0)]

# Test with different thresholds
for threshold in [0.5, 1, 2]:
    simplified_points = douglas_peucker(test_points, threshold)
    print(f"Threshold: {threshold}, Simplified Points: {simplified_points}")

    # Extract x and y coordinates for plotting
    initial_x, initial_y = zip(*test_points)
    simplified_x, simplified_y = zip(*simplified_points)

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot the initial points
    plt.plot(initial_x, initial_y, 'bo-', label='Initial Points')

    # Plot the simplified path
    plt.plot(simplified_x, simplified_y, 'ro-', label=f'Simplified Path (Threshold = {threshold})')

    # Labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Initial and Simplified Path (Threshold = {threshold})')

    # Display legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

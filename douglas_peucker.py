
from distance_point_line import distance

def douglas_peucker(points, threshold):
    """
    Simplify a polyline using the Douglas-Peucker algorithm.

    Args:
        points (list): A list of points (x, y) defining the polyline.
        threshold (float): The distance threshold for simplification.

    Returns:
        list: A simplified list of points.
    """
    if len(points) < 3:
        return points

    # Line defined by the first and last points
    start, end = points[0], points[-1]
    max_distance = 0
    index = 0

    # Find the point with the maximum distance to the line
    for i in range(1, len(points) - 1):
        dist = distance(points[i], (start, end))
        if dist > max_distance:
            max_distance = dist
            index = i

    # If the max distance is greater than the threshold, recursively simplify
    if max_distance > threshold:
        left = douglas_peucker(points[:index + 1], threshold)
        right = douglas_peucker(points[index:], threshold)
        return left[:-1] + right

    # Otherwise, return the start and end points
    return [start, end]

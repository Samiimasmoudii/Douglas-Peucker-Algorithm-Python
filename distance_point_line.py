import math
from slope import slope
from intercept import y_intercept

def distance(point, line):
    """
    Calculate the perpendicular distance from a point to a line.

    Args:
        point (tuple): The point (x_A, y_A).
        line (tuple): A tuple containing two points that define the line ((x1, y1), (x2, y2)).

    Returns:
        float: The perpendicular distance from the point to the line.
    """
    x_A, y_A = point
    (x1, y1), (x2, y2) = line

    # Handle vertical line
    if x1 == x2:
        return abs(x_A - x1)

    # Handle horizontal line
    if y1 == y2:
        return abs(y_A - y1)

    # Calculate slope and y-intercept of the line
    p = slope((x1, y1), (x2, y2))
    m = y_intercept((x1, y1), p)

    # Calculate distance using the given formula
    return abs(p * x_A - y_A + m) / math.sqrt(1 + p**2)

def slope(point1, point2):
    """
    Calculate the slope of a line given two points.

    Args:
        point1 (tuple): First point (x1, y1).
        point2 (tuple): Second point (x2, y2).

    Returns:
        float: The slope of the line.
    """
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        return None  # Vertical line
    return (y2 - y1) / (x2 - x1)

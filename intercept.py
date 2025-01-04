
def y_intercept(point, slope):
    """
    Calculate the y-intercept of a line given a point and its slope.

    Args:
        point (tuple): A point (x, y) on the line.
        slope (float): The slope of the line.

    Returns:
        float: The y-intercept of the line.
    """
    x, y = point
    if slope is None:
        return None  # Vertical line
    return y - slope * x

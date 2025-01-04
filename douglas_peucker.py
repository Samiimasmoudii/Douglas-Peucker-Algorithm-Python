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
    # Si aucun point ou moins de 3 points, on termine
    if len(points) < 3:
        return points

    # Ligne définie par le premier et le dernier point
    start, end = points[0], points[-1]
    max_distance = 0
    index = 0

    # Trouver le point avec la distance maximale par rapport à la ligne
    for i in range(1, len(points) - 1):
        dist = distance(points[i], (start, end))
        if dist > max_distance:
            max_distance = dist
            index = i

    # Si la distance maximale est inférieure ou égale au seuil, on supprime les points intermédiaires
    if max_distance <= threshold:
        return [start, end]

    # Sinon, on divise la polyligne en deux parties et on répète l'opération récursivement
    left = douglas_peucker(points[:index + 1], threshold)
    right = douglas_peucker(points[index:], threshold)
    
    # On retourne la fusion des deux parties simplifiées, en évitant de dupliquer le point de jonction
    return left[:-1] + right

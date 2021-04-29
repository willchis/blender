from mathutils import Vector

def distance_vec(point1: Vector, point2: Vector) -> float: 
    """Calculate distance between two points.""" 
    return (point2 - point1).length   

import math

from mathutils import Vector, Quaternion, Matrix

def clamp(val, min_val, max_val):

    return max(min_val, min(val, max_val))

def lerp(a, b, t):

    return (1 - t) * a + t * b

def apply_drag(velocity, drag_factor):

    """Applies a simple drag to a velocity vector [x, y, z]"""

    velocity[0] *= drag_factor

    velocity[1] *= drag_factor

    velocity[2] *= drag_factor

    return velocity

def get_view_matrix(context):

    for area in context.screen.areas:

        if area.type == 'VIEW_3D':

            region_3d = area.spaces[0].region_3d

            return region_3d.view_matrix.copy()

    return None

def rotate_point(point, angle_x=0.0, angle_y=0.0, angle_z=0.0):

    """Rotate a point by given local angles"""

    pass

def apply_deadzone(value, deadzone):

    if abs(value) < deadzone:

        return 0.0

    return (value - deadzone * (1 if value > 0 else -1)) / (1.0 - deadzone)


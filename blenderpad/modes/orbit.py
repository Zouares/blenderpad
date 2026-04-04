import bpy

from ..utils.math_utils import clamp

from mathutils import Matrix, Vector

class OrbitMode:

    @staticmethod

    def tick(context, prefs, inputs, view3d_region, region_3d):

        pan_speed_mult = prefs.pan_speed

        orbit_speed_mult = prefs.orbit_speed

        zoom_speed_mult = prefs.zoom_speed

        lx = inputs['left_stick_x']

        ly = -inputs['left_stick_y']                        

        rx = inputs['right_stick_x']

        ry = inputs['right_stick_y']

        lt = inputs['left_trigger']

        rt = inputs['right_trigger']

        if abs(rx) > 0.01 or abs(ry) > 0.01:

            override = get_view3d_override(context)

            if override:

                rot = region_3d.view_rotation.to_euler()

                rot.z -= rx * 0.05 * orbit_speed_mult

                rot.x -= ry * 0.05 * orbit_speed_mult

                region_3d.view_rotation = rot.to_quaternion()

        if abs(lx) > 0.01 or abs(ly) > 0.01:

            view_inv = region_3d.view_matrix.inverted().to_3x3()

            pan_vec = Vector((lx, ly, 0.0)) * 0.1 * pan_speed_mult * region_3d.view_distance

            global_pan = view_inv @ pan_vec

            region_3d.view_location += global_pan

        if rt > 0.01:

            region_3d.view_distance -= rt * 0.5 * zoom_speed_mult * (region_3d.view_distance * 0.1)

        if lt > 0.01:

            region_3d.view_distance += lt * 0.5 * zoom_speed_mult * (region_3d.view_distance * 0.1)

        region_3d.view_distance = max(region_3d.view_distance, 0.001)

def get_view3d_override(context):

    for area in context.screen.areas:

        if area.type == 'VIEW_3D':

            for region in area.regions:

                if region.type == 'WINDOW':

                    override = context.copy()

                    override['area'] = area

                    override['region'] = region

                    override['space_data'] = area.spaces.active

                    return override

    return None


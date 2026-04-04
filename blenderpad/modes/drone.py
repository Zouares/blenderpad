import bpy

from mathutils import Vector, Matrix, Euler

from ..core.state import addon_state

class DroneMode:

    @staticmethod

    def tick(context, prefs, inputs, view3d_region, region_3d):

        speed_mult = prefs.drone_speed

        if inputs['buttons']['RB']:

            speed_mult *= 2.0         

        elif inputs['buttons']['LB']:

            speed_mult *= 0.2             

        move_camera = prefs.drone_move_camera

        cam = context.scene.camera if move_camera else None

        ly = inputs['left_stick_y']                    

        lx = inputs['left_stick_x']                     

        ry = inputs['right_stick_y']        

        rx = inputs['right_stick_x']      

        if prefs.invert_move_y:

            ly = -ly

        if prefs.invert_look_y:

            ry = -ry

        rt = inputs['right_trigger']         

        lt = inputs['left_trigger']           

        target_vel = Vector((lx, -lt + rt, ly)) * 0.1 * speed_mult

        if prefs.drone_use_inertia:

            inertia = prefs.drone_inertia

            addon_state.drone_velocity[0] = addon_state.drone_velocity[0] * inertia + target_vel.x * (1.0 - inertia)

            addon_state.drone_velocity[1] = addon_state.drone_velocity[1] * inertia + target_vel.y * (1.0 - inertia)

            addon_state.drone_velocity[2] = addon_state.drone_velocity[2] * inertia + target_vel.z * (1.0 - inertia)

        else:

            addon_state.drone_velocity = [target_vel.x, target_vel.y, target_vel.z]

        vel_vec = Vector(addon_state.drone_velocity)

        if move_camera and cam:

            orient_mat = cam.matrix_world.to_3x3()

        else:

            orient_mat = region_3d.view_matrix.inverted().to_3x3()

        if prefs.drone_altitude_hold:

            stick_vel = Vector((vel_vec.x, 0.0, vel_vec.z))

            mapped_stick = orient_mat @ stick_vel

            mapped_stick.z = 0.0

            trigger_vertical = Vector((0.0, 0.0, vel_vec.y))

            global_vel = mapped_stick + trigger_vertical

        else:

            global_vel = orient_mat @ vel_vec

        if move_camera and cam:

            cam.rotation_euler.z -= rx * 0.05

            cam.rotation_euler.x -= ry * 0.05

            cam.location += global_vel

            if prefs.drone_auto_keyframe:

                cam.keyframe_insert(data_path="location", frame=context.scene.frame_current)

                cam.keyframe_insert(data_path="rotation_euler", frame=context.scene.frame_current)

                context.scene.frame_current += 1

        else:

            rot = region_3d.view_rotation.to_euler()

            rot.z -= rx * 0.05

            rot.x -= ry * 0.05

            rot.x = max(min(rot.x, 1.57), -1.57)

            region_3d.view_rotation = rot.to_quaternion()

            region_3d.view_location += global_vel


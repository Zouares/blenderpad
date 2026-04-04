import bpy

from .input_manager import gamepad_manager, PYGAME_AVAILABLE

from .state import addon_state

from ..modes.orbit import OrbitMode

from ..modes.drone import DroneMode

class BlenderPadEngine:

    @staticmethod

    def timer_tick():

        if not addon_state.is_running:

            return None

        context = bpy.context

        view3d_area = None

        view3d_region = None

        region_3d = None

        for area in context.screen.areas:

            if area.type == 'VIEW_3D':

                view3d_area = area

                for region in area.regions:

                    if region.type == 'WINDOW':

                        view3d_region = region

                        region_3d = area.spaces[0].region_3d

                        break

                break

        if not region_3d:

            gamepad_manager.poll()

            return 0.016

        from ..ui.prefs import get_addon_preferences

        prefs = get_addon_preferences(context)

        gamepad_manager.deadzone_l = prefs.deadzone

        gamepad_manager.deadzone_r = prefs.deadzone

        gamepad_manager.smoothing = prefs.smoothing

        gamepad_manager.poll()

        inputs = gamepad_manager.state

        try:

            if addon_state.active_mode == "ORBITAL":

                OrbitMode.tick(context, prefs, inputs, view3d_region, region_3d)

            elif addon_state.active_mode == "DRONE":

                DroneMode.tick(context, prefs, inputs, view3d_region, region_3d)

        except Exception as e:

            print("BlenderPad Error in Tick:", e)

        if view3d_area:

            view3d_area.tag_redraw()

        return 0.016                

def on_button_pressed(btn_name):

    print("Pressed:", btn_name)

    context = bpy.context

    if btn_name == "A":

        bpy.ops.view3d.view_selected('INVOKE_DEFAULT')

    elif btn_name == "L3":

        addon_state.active_mode = "DRONE"

        context.scene.blenderpad_mode = "DRONE"

    elif btn_name == "R3":

        addon_state.active_mode = "FPS"

        context.scene.blenderpad_mode = "FPS"

gamepad_manager.add_callback('on_button_pressed', on_button_pressed)

class BLENDERPAD_OT_start(bpy.types.Operator):

    """Start polling gamepads"""

    bl_idname = "blenderpad.start"

    bl_label = "Start Gamepad Polling"

    bl_options = {'REGISTER'}

    def execute(self, context):

        if not PYGAME_AVAILABLE:

            self.report({'ERROR'}, "Pygame not available. Install it first.")

            return {'CANCELLED'}

        if not addon_state.is_running:

            addon_state.is_running = True

            bpy.app.timers.register(BlenderPadEngine.timer_tick)

            self.report({'INFO'}, "BlenderPad Started")

        return {'FINISHED'}

class BLENDERPAD_OT_stop(bpy.types.Operator):

    """Stop polling gamepads"""

    bl_idname = "blenderpad.stop"

    bl_label = "Stop Gamepad Polling"

    bl_options = {'REGISTER'}

    def execute(self, context):

        if addon_state.is_running:

            addon_state.is_running = False

            self.report({'INFO'}, "BlenderPad Stopped")

        addon_state.drone_velocity = [0.0, 0.0, 0.0]

        return {'FINISHED'}

def register():

    bpy.utils.register_class(BLENDERPAD_OT_start)

    bpy.utils.register_class(BLENDERPAD_OT_stop)

def unregister():

    bpy.utils.unregister_class(BLENDERPAD_OT_start)

    bpy.utils.unregister_class(BLENDERPAD_OT_stop)

    if addon_state.is_running:

        addon_state.is_running = False


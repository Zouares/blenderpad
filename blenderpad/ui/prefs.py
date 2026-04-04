import bpy

from ..core.input_manager import PYGAME_AVAILABLE

class BLENDERPAD_Settings(bpy.types.PropertyGroup):

    orbit_speed: bpy.props.FloatProperty(name="Orbit Speed", default=1.0, min=0.1, max=5.0)

    pan_speed: bpy.props.FloatProperty(name="Pan Speed", default=1.0, min=0.1, max=5.0)

    zoom_speed: bpy.props.FloatProperty(name="Zoom Speed", default=1.0, min=0.1, max=5.0)

    drone_speed: bpy.props.FloatProperty(name="Drone Speed", default=5.0, min=0.1, max=50.0)

    drone_inertia: bpy.props.FloatProperty(name="Drone Inertia", default=0.85, min=0.0, max=0.99)

    drone_altitude_hold: bpy.props.BoolProperty(name="Altitude Hold", default=True)

    drone_use_inertia: bpy.props.BoolProperty(name="Use Inertia", default=True)

    deadzone: bpy.props.FloatProperty(name="Deadzone", default=0.15, min=0.0, max=0.8)

    smoothing: bpy.props.FloatProperty(name="Smoothing (EWMA)", default=0.30, min=0.0, max=0.99)

    invert_look_y: bpy.props.BoolProperty(name="Invert Look Y", default=False)

    invert_move_y: bpy.props.BoolProperty(name="Invert Move Y", default=False)

    drone_move_camera: bpy.props.BoolProperty(name="Move Active Camera in Drone", default=True)

    drone_auto_keyframe: bpy.props.BoolProperty(name="Auto Keyframe on Move", default=False)

    fps_eye_height: bpy.props.FloatProperty(name="FPS Eye Height", default=1.7, min=0.1, max=5.0)

def get_addon_preferences(context):

    return context.scene.blenderpad_settings

def register():

    bpy.utils.register_class(BLENDERPAD_Settings)

    bpy.types.Scene.blenderpad_settings = bpy.props.PointerProperty(type=BLENDERPAD_Settings)

def unregister():

    bpy.utils.unregister_class(BLENDERPAD_Settings)

    if hasattr(bpy.types.Scene, "blenderpad_settings"):

        del bpy.types.Scene.blenderpad_settings


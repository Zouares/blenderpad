import bpy

from ..core.input_manager import PYGAME_AVAILABLE, gamepad_manager

from ..core.state import addon_state

from .prefs import get_addon_preferences

class BLENDERPAD_PT_main_panel(bpy.types.Panel):

    bl_label = "Gamepad Setup"

    bl_idname = "BLENDERPAD_PT_main_panel"

    bl_space_type = 'VIEW_3D'

    bl_region_type = 'UI'

    bl_category = 'Gamepad'

    def draw(self, context):

        layout = self.layout

        prefs = get_addon_preferences(context)

        if not PYGAME_AVAILABLE:

            box = layout.box()

            box.label(text="Dependencies Missing!", icon='ERROR')

            box.operator("blenderpad.install_pygame", text="Install Pygame", icon='IMPORT')

            return

        box = layout.box()

        if gamepad_manager.active_joystick:

            name = gamepad_manager.active_joystick.get_name()

            box.label(text=f"Connected: {name}", icon='CON_TRACKTO')

        else:

            box.label(text="No controller detected.", icon='ERROR')

        row = box.row()

        if addon_state.is_running:

            row.operator("blenderpad.stop", text="Stop Engine", icon='PAUSE')

        else:

            row.operator("blenderpad.start", text="Start Engine", icon='PLAY')

        layout.separator()

        layout.label(text="Current Mode:", icon='VIEW3D')

        row = layout.row(align=True)

        row.prop_enum(context.scene, "blenderpad_mode", "ORBITAL")

        row.prop_enum(context.scene, "blenderpad_mode", "DRONE")

        if hasattr(context.scene, "blenderpad_mode"):

            addon_state.active_mode = context.scene.blenderpad_mode

        box = layout.box()

        box.label(text="Sensitivities:", icon='PREFERENCES')

        col = box.column(align=True)

        if addon_state.active_mode == "ORBITAL":

            col.prop(prefs, "orbit_speed")

            col.prop(prefs, "pan_speed")

            col.prop(prefs, "zoom_speed")

        elif addon_state.active_mode == "DRONE":

            col.prop(prefs, "drone_speed")

            col.prop(prefs, "drone_inertia")

            box2 = layout.box()

            box2.label(text="Drone Physics:")

            box2.prop(prefs, "drone_altitude_hold")

            box2.prop(prefs, "drone_use_inertia")

            box3 = layout.box()

            box3.label(text="Camera Settings:")

            box3.prop(prefs, "drone_move_camera")

            box3.prop(prefs, "drone_auto_keyframe")

        layout.separator()

        box = layout.box()

        box.label(text="Controls & Filters:", icon='PREFERENCES')

        col = box.column(align=True)

        col.prop(prefs, "deadzone")

        col.prop(prefs, "smoothing")

        col.separator()

        row_invert = col.row()

        row_invert.prop(prefs, "invert_look_y", toggle=True)

        row_invert.prop(prefs, "invert_move_y", toggle=True)

def register():

    bpy.types.Scene.blenderpad_mode = bpy.props.EnumProperty(

        items=[

            ("ORBITAL", "Orbital", "Orbit around the view"),

            ("DRONE", "Drone", "Fly freely in 3D space")

        ],

        name="Mode",

        default="ORBITAL"

    )

    bpy.utils.register_class(BLENDERPAD_PT_main_panel)

def unregister():

    bpy.utils.unregister_class(BLENDERPAD_PT_main_panel)

    if hasattr(bpy.types.Scene, "blenderpad_mode"):

        del bpy.types.Scene.blenderpad_mode


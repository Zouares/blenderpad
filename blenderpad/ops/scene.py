import bpy

import bmesh

def select_all(context):

    if context.active_object and context.active_object.mode == 'EDIT':

        bpy.ops.mesh.select_all(action='TOGGLE')

    else:

        bpy.ops.object.select_all(action='TOGGLE')

def duplicate_selected(context):

    if context.active_object and context.active_object.mode != 'EDIT':

        bpy.ops.object.duplicate_move()

def delete_selected(context):

    if context.active_object:

        if context.active_object.mode == 'EDIT':

            bpy.ops.mesh.delete()

        else:

            bpy.ops.object.delete()

def apply_transforms(context):

    if context.active_object and context.active_object.mode != 'EDIT':

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

def render_frame(context):

    bpy.ops.render.render('INVOKE_DEFAULT')

def render_anim(context):

    bpy.ops.render.render('INVOKE_DEFAULT', animation=True)

class BLENDERPAD_OT_scene_action(bpy.types.Operator):

    """Execute a scene action from Gamepad"""

    bl_idname = "blenderpad.scene_action"

    bl_label = "Gamepad Scene Action"

    bl_options = {'REGISTER', 'UNDO'}

    action: bpy.props.StringProperty()

    def execute(self, context):

        if self.action == 'SELECT_ALL':

            select_all(context)

        elif self.action == 'DUPLICATE':

            duplicate_selected(context)

        elif self.action == 'DELETE':

            delete_selected(context)

        elif self.action == 'APPLY_TRANSFORM':

            apply_transforms(context)

        elif self.action == 'RENDER_FRAME':

            render_frame(context)

        elif self.action == 'RENDER_ANIM':

            render_anim(context)

        return {'FINISHED'}

def register():

    bpy.utils.register_class(BLENDERPAD_OT_scene_action)

def unregister():

    bpy.utils.unregister_class(BLENDERPAD_OT_scene_action)


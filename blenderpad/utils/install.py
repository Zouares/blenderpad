import sys

import subprocess

import bpy

def install_package(package_name):

    """Installs a python package via pip in Blender's bundled python."""

    py_exec = sys.executable

    try:

        subprocess.check_call([py_exec, "-m", "pip", "install", package_name])

        return True

    except subprocess.CalledProcessError:

        return False

def check_pygame():

    """Checks if pygame is installed, returns True if it is."""

    try:

        import pygame

        return True

    except ImportError:

        return False

class BLENDERPAD_OT_install_pygame(bpy.types.Operator):

    """Install Pygame for Gamepad Navigation"""

    bl_idname = "blenderpad.install_pygame"

    bl_label = "Install Pygame"

    bl_description = "Installs the pygame library required for gamepad input"

    bl_options = {'REGISTER'}

    def execute(self, context):

        self.report({'INFO'}, "Installing pygame, please wait...")

        success = install_package("pygame")

        if success:

            self.report({'INFO'}, "Pygame installed successfully!")

        else:

            self.report({'ERROR'}, "Failed to install pygame. See console.")

        return {'FINISHED'}

def register():

    bpy.utils.register_class(BLENDERPAD_OT_install_pygame)

def unregister():

    bpy.utils.unregister_class(BLENDERPAD_OT_install_pygame)


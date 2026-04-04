bl_info = {
    "name": "BlenderPad",
    "author": "Zouares",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "View3D > N-Panel > Gamepad",
    "description": "Gamepad navigation engine for Blender",
    "category": "Viewport Control",
}

import bpy
from .core import register as register_core, unregister as unregister_core
from .utils.install import register as register_install, unregister as unregister_install
from .ui.prefs import register as register_prefs, unregister as unregister_prefs
from .ui.panel import register as register_panel, unregister as unregister_panel
from .ops.scene import register as register_scene_ops, unregister as unregister_scene_ops

_modules = [
    register_install,
    register_prefs,
    register_scene_ops,
    register_core,
    register_panel,
]

_unmodules = [
    unregister_panel,
    unregister_core,
    unregister_scene_ops,
    unregister_prefs,
    unregister_install,
]

def register():
    for m in _modules:
        m()

def unregister():
    for m in _unmodules:
        m()

if __name__ == "__main__":
    register()

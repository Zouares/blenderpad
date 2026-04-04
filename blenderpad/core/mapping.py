import bpy

class GamepadAction:

    NONE = "NONE"

    ORBIT_PAN_LEFT = "ORBIT_PAN_LEFT"

    FOCUS_SELECTED = "FOCUS_SELECTED"

    TOGGLE_PERSP_ORTHO = "TOGGLE_PERSP_ORTHO"

    FRONT_VIEW = "FRONT_VIEW"

    TOP_VIEW = "TOP_VIEW"

    CAMERA_VIEW = "CAMERA_VIEW"

    MODE_ORBITAL = "MODE_ORBITAL"

    MODE_DRONE = "MODE_DRONE"

    MODE_FPS = "MODE_FPS"

    DRONE_CONFIRM = "DRONE_CONFIRM"

    DRONE_CANCEL = "DRONE_CANCEL"

    DRONE_PRECISION = "DRONE_PRECISION"

    DRONE_TURBO = "DRONE_TURBO"

    DRONE_TOGGLE_TARGET = "DRONE_TOGGLE_TARGET"

    FPS_JUMP = "FPS_JUMP"

    FPS_CROUCH = "FPS_CROUCH"

    FPS_TOGGLE_FLY = "FPS_TOGGLE_FLY"

    FPS_TOGGLE_COLLISION = "FPS_TOGGLE_COLLISION"

    FPS_TOGGLE_GRAVITY = "FPS_TOGGLE_GRAVITY"

    FPS_RESET = "FPS_RESET"

    FPS_SNAPSHOT = "FPS_SNAPSHOT"

    SELECT_ALL = "SELECT_ALL"

    BOX_SELECT = "BOX_SELECT"

    DUPLICATE = "DUPLICATE"

    DELETE = "DELETE"

    APPLY_TRANSFORM = "APPLY_TRANSFORM"

    RENDER_FRAME = "RENDER_FRAME"

    RENDER_ANIM = "RENDER_ANIM"

default_button_map = {

    'A': GamepadAction.FOCUS_SELECTED,

    'B': GamepadAction.TOGGLE_PERSP_ORTHO,

    'X': GamepadAction.TOP_VIEW,

    'Y': GamepadAction.FRONT_VIEW,

    'START': GamepadAction.CAMERA_VIEW,

    'SELECT': GamepadAction.NONE,

    'L3': GamepadAction.MODE_DRONE,

    'R3': GamepadAction.MODE_FPS,

    'LB': GamepadAction.NONE,

    'RB': GamepadAction.NONE,

    'DPAD_UP': GamepadAction.NONE,

    'DPAD_DOWN': GamepadAction.NONE,

    'DPAD_LEFT': GamepadAction.NONE,

    'DPAD_RIGHT': GamepadAction.NONE,

}

default_drone_map = {

    'A': GamepadAction.DRONE_CONFIRM,

    'B': GamepadAction.DRONE_CANCEL,

    'START': GamepadAction.DRONE_TOGGLE_TARGET,

    'L3': GamepadAction.MODE_ORBITAL,

    'R3': GamepadAction.MODE_FPS,

}

default_fps_map = {

    'A': GamepadAction.FPS_JUMP,

    'B': GamepadAction.FPS_CROUCH,

    'Y': GamepadAction.FPS_TOGGLE_GRAVITY,

    'X': GamepadAction.FPS_RESET,

    'START': GamepadAction.CAMERA_VIEW,

    'SELECT': GamepadAction.FPS_SNAPSHOT,

    'L3': GamepadAction.MODE_ORBITAL,

    'R3': GamepadAction.MODE_DRONE,

    'LB': GamepadAction.FPS_TOGGLE_FLY,

    'RB': GamepadAction.FPS_TOGGLE_COLLISION,

}


import bpy

class AddonState:

    def __init__(self):

        self.active_mode = "ORBITAL"                      

        self.is_running = False

        self.timer_func = None

        self.drone_velocity = [0.0, 0.0, 0.0]

        self.fps_is_fly_mode = False

        self.fps_velocity = [0.0, 0.0, 0.0]

        self.fps_falling_speed = 0.0

addon_state = AddonState()


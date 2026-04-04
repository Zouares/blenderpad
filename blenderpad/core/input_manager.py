import os

import copy

from ..utils.install import check_pygame

try:

    import pygame

    PYGAME_AVAILABLE = True

except ImportError:

    PYGAME_AVAILABLE = False

class GamepadManager:

    def __init__(self):

        self.joysticks = []

        self.active_joystick = None

        self.active_joystick_index = 0

        self.deadzone_l = 0.15

        self.deadzone_r = 0.15

        self.smoothing = 0.30

        self.state = {

            'left_stick_x': 0.0,

            'left_stick_y': 0.0,

            'right_stick_x': 0.0,

            'right_stick_y': 0.0,

            'left_trigger': 0.0,

            'right_trigger': 0.0,

            'buttons': {

                'A': False, 'B': False, 'X': False, 'Y': False,

                'LB': False, 'RB': False, 'START': False, 'SELECT': False,

                'L3': False, 'R3': False,

                'DPAD_UP': False, 'DPAD_DOWN': False,

                'DPAD_LEFT': False, 'DPAD_RIGHT': False,

            }

        }

        self.previous_buttons = {k: False for k in self.state['buttons']}

        self.callbacks = {

            'on_button_pressed': [],

            'on_button_released': []

        }

        if PYGAME_AVAILABLE:

            os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

            try:

                pygame.joystick.init()

                pygame.display.init()

            except Exception:

                pass

            self.refresh_joysticks()

    def add_callback(self, event, func):

        if event in self.callbacks:

            self.callbacks[event].append(func)

    def refresh_joysticks(self):

        if not PYGAME_AVAILABLE:

            return

        self.joysticks = []

        for i in range(pygame.joystick.get_count()):

            try:

                joy = pygame.joystick.Joystick(i)

                joy.init()

                self.joysticks.append(joy)

            except Exception:

                pass

        if self.joysticks and self.active_joystick is None:

            self.set_active_joystick(0)

    def set_active_joystick(self, index):

        if 0 <= index < len(self.joysticks):

            self.active_joystick = self.joysticks[index]

            self.active_joystick_index = index

    def apply_deadzone(self, value, deadzone):

        if abs(value) < deadzone:

            return 0.0

        return (value - deadzone * (1 if value > 0 else -1)) / (1.0 - deadzone)

    def exponential_smoothing(self, current, new_val, alpha):

        return current * alpha + new_val * (1.0 - alpha)

    def poll(self):

        if not PYGAME_AVAILABLE:

            return

        pygame.event.pump()

        if not self.active_joystick:

            self.refresh_joysticks()

            if not self.active_joystick:

                return

        try:

            lx = self.active_joystick.get_axis(0)

            ly = self.active_joystick.get_axis(1)

            num_axes = self.active_joystick.get_numaxes()

            rx, ry, lt, rt = 0.0, 0.0, -1.0, -1.0

            if num_axes >= 6:

                rx = self.active_joystick.get_axis(2) if num_axes > 3 else 0.0

                ry = self.active_joystick.get_axis(3) if num_axes > 3 else 0.0

                lt = self.active_joystick.get_axis(4) if num_axes > 4 else 0.0

                rt = self.active_joystick.get_axis(5) if num_axes > 5 else 0.0

            lt_mapped = (lt + 1.0) / 2.0

            rt_mapped = (rt + 1.0) / 2.0

            lx = self.apply_deadzone(lx, self.deadzone_l)

            ly = self.apply_deadzone(ly, self.deadzone_l)

            rx = self.apply_deadzone(rx, self.deadzone_r)

            ry = self.apply_deadzone(ry, self.deadzone_r)

            alpha = self.smoothing

            self.state['left_stick_x'] = self.exponential_smoothing(self.state['left_stick_x'], lx, alpha)

            self.state['left_stick_y'] = self.exponential_smoothing(self.state['left_stick_y'], ly, alpha)

            self.state['right_stick_x'] = self.exponential_smoothing(self.state['right_stick_x'], rx, alpha)

            self.state['right_stick_y'] = self.exponential_smoothing(self.state['right_stick_y'], ry, alpha)

            self.state['left_trigger'] = lt_mapped

            self.state['right_trigger'] = rt_mapped

            mapping = {

                'A': 0, 'B': 1, 'X': 2, 'Y': 3,

                'LB': 4, 'RB': 5, 'SELECT': 6, 'START': 7,

                'L3': 8, 'R3': 9

            }

            num_btns = self.active_joystick.get_numbuttons()

            for btn_name, btn_idx in mapping.items():

                if btn_idx < num_btns:

                    val = self.active_joystick.get_button(btn_idx)

                    self.state['buttons'][btn_name] = bool(val)

            if self.active_joystick.get_numhats() > 0:

                hat = self.active_joystick.get_hat(0)

                self.state['buttons']['DPAD_LEFT'] = (hat[0] == -1)

                self.state['buttons']['DPAD_RIGHT'] = (hat[0] == 1)

                self.state['buttons']['DPAD_DOWN'] = (hat[1] == -1)

                self.state['buttons']['DPAD_UP'] = (hat[1] == 1)

            for btn_name, is_pressed in self.state['buttons'].items():

                was_pressed = self.previous_buttons[btn_name]

                if is_pressed and not was_pressed:

                    for cb in self.callbacks['on_button_pressed']:

                        cb(btn_name)

                elif not is_pressed and was_pressed:

                    for cb in self.callbacks['on_button_released']:

                        cb(btn_name)

                self.previous_buttons[btn_name] = is_pressed

        except Exception as e:

            print("Gamepad error:", e)

gamepad_manager = GamepadManager()


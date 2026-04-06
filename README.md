# BlenderPad

> Control Blender viewport and scene with gamepad controllers.

![Blender](https://img.shields.io/badge/Blender-4.2%2B-orange?logo=blender)
![License](https://img.shields.io/badge/License-GPL--2.0-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-green)

---

## Features

| Feature | Description |
|---|---|
| **Orbital Mode** | Smooth viewport navigation (Orbit, Pan, Zoom) using thumbsticks |
| **Drone Mode** | Fly freely in 3D space with cinematic inertia and altitude hold |
| **Active Camera** | Move the actual scene camera in real-time with auto-keyframing |
| **Sensitivity Tuning** | Dedicated N-Panel settings for speed, deadzone, and smoothing |
| **Axis Inversion** | Quick toggles for inverting Look and Move Y axes |
| **Altitude Hold** | Fixed-height horizontal flight — perfect for architectural walkthroughs |
| **Native Extension** | Built for Blender 4.2+ and 5.0+ extension system |

---

## Installation

### From Zip (Blender 4.2+ Preferences)

1. Download the latest `blenderpad.zip` from [Releases](../../releases)
2. Open Blender → **Edit → Preferences → Get Extensions**
3. Click the **arrow** next to the "Install" button → **Install from Disk...**
4. Select `blenderpad.zip` and click **Install**
5. Go to the **Gamepad** tab in the 3D Viewport N-Panel and click **"Install Pygame"** if missing.

### From Source

```bash
git clone https://github.com/Zouares/blenderpad.git
```

Copy the `blenderpad/` folder into your Blender extensions directory:

| OS | Path |
|---|---|
| Windows | `%APPDATA%\Blender Foundation\Blender\5.0\extensions\user_default\` |
| macOS | `~/Library/Application Support/Blender/5.0/extensions/user_default/` |
| Linux | `~/.config/blender/5.0/extensions/user_default/` |

---

## Usage

1. Open the **N Panel** in the 3D Viewport (`N` key)
2. Go to the **"Gamepad"** tab
3. Click **Start Engine** to begin polling input
4. Choose your mode: **Orbital** or **Drone**
5. Adjust **Sensitivities** and **Filters** to match your controller's feel

### Controller Reference (Drone Mode)

| Input | Action |
|---|---|
| **Left Stick** | Forward / Backward & Strafe Left / Right |
| **Right Stick** | Yaw (Rotate) & Pitch (Tilt) |
| **RT / LT** | Ascend / Descend |
| **RB / LB** | Turbo Speed / Precision Speed |
| **A Button** | Frame Selected (View) |
| **L3 / R3** | Switch to Drone / Switch to Orbital |

---

## Project Structure

```
blenderpad/
├── __init__.py            # Module registration & bl_info
├── blender_manifest.toml  # Extension metadata
├── README.md              # Documentation
├── core/
│   ├── input_manager.py   # Pygame polling and deadzone logic
│   ├── mapping.py         # Controller button bindings
│   └── state.py           # Engine runtime state
├── modes/
│   ├── orbit.py           # Orbital navigation logic
│   └── drone.py           # Free flight with altitude hold
├── ui/
│   ├── panel.py           # N-Panel UI definition
│   └── prefs.py           # PropertyGroup & sensitivity settings
└── utils/
    ├── install.py         # Pygame dependency installer
    └── math_utils.py      # Vector transformation helpers
```

---

## Compatibility

| Blender Version | Status |
|---|---|
| 4.2 LTS | ✅ Tested |
| 4.3 | ✅ Tested |
| 5.0+ | ✅ Tested |

---

## Contributing

Pull requests are welcome! Please open an issue first to discuss what you would like to change.

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
```

# Contributing to BlenderPad

Thank you for your interest in contributing! This document explains how to set up your environment, the project structure, and the conventions used throughout the codebase.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Coding Conventions](#coding-conventions)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Adding a New Mode](#adding-a-new-mode)
- [Adding Controller Bindings](#adding-controller-bindings)

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/blenderpad.git
   ```
3. Create a **feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes, commit, and push:
   ```bash
   git commit -m "Add: short description of your change"
   git push origin feature/your-feature-name
   ```
5. Open a **Pull Request** against `main`.

> **Please open an issue first** to discuss larger changes before investing time in an implementation. This avoids duplicate work and ensures the change aligns with the project's direction.

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

| Module | Responsibility |
|---|---|
| `core/input_manager.py` | Pygame event loop, deadzone filtering, axis normalization |
| `core/mapping.py` | Button and axis bindings — the single source of truth for controller layout |
| `core/state.py` | Shared runtime state (engine running, active mode, smoothed values) |
| `modes/orbit.py` | Viewport orbit, pan, and zoom logic |
| `modes/drone.py` | Free-flight with inertia, altitude hold, and turbo/precision speeds |
| `ui/panel.py` | N-Panel layout (Start/Stop Engine, mode switcher, sensitivity controls) |
| `ui/prefs.py` | `PropertyGroup` for all user-facing settings |
| `utils/install.py` | In-Blender Pygame installer triggered from the N-Panel |
| `utils/math_utils.py` | Reusable vector math helpers (smoothing, coordinate transforms) |

---

## Development Setup

### Requirements

- **Blender 4.2 LTS or later** (4.3, 5.0+ are also tested)
- **Pygame** — installed automatically via the **"Install Pygame"** button in the Gamepad N-Panel, or manually:
  ```bash
  # Using Blender's bundled Python
  /path/to/blender/python/bin/python -m pip install pygame
  ```

### Installing from Source

Copy (or symlink) the `blenderpad/` folder into your Blender extensions directory:

| OS | Path |
|---|---|
| Windows | `%APPDATA%\Blender Foundation\Blender\5.0\extensions\user_default\` |
| macOS | `~/Library/Application Support/Blender/5.0/extensions/user_default/` |
| Linux | `~/.config/blender/5.0/extensions/user_default/` |

Then enable it under **Edit → Preferences → Get Extensions**.

### Reloading During Development

Use **Reload Scripts** (`F3` → "Reload Scripts") to pick up code changes without restarting Blender. Note that the gamepad engine must be stopped (`Stop Engine`) before reloading to avoid orphaned Pygame threads.

---

## Coding Conventions

- **Style:** Follow [PEP 8](https://peps.python.org/pep-0008/). Use 4-space indentation.
- **Operator naming:** Use the `blenderpad.` prefix for all `bl_idname` values (e.g. `blenderpad.start_engine`).
- **State access:** Always read and write engine state through `core/state.py` — do not store mutable runtime state on the operator or panel classes directly.
- **Input polling:** All Pygame calls must stay inside `core/input_manager.py`. Modes receive normalized, deadzone-filtered values — they never call Pygame directly.
- **Math helpers:** Add reusable vector/math utilities to `utils/math_utils.py` rather than inlining them in mode files.
- **Thread safety:** The Pygame polling loop runs in a modal operator. Use Blender's modal timer pattern — never spawn raw Python threads.
- **Commits:** Use an imperative prefix: `Add:`, `Fix:`, `Refactor:`, `Docs:`, `Chore:`.

---

## Submitting Changes

- Keep pull requests **focused** — one feature or fix per PR.
- Describe *what* changed and *why* in the PR description.
- If your PR closes an issue, include `Closes #<issue-number>` in the description.
- Make sure the addon registers and unregisters cleanly — check the Blender system console for errors.
- Test the gamepad engine with **Start Engine** / **Stop Engine** across at least one mode.
- Test against **Blender 4.2 LTS** as the minimum supported version.

---

## Reporting Issues

When filing a bug, please include:

1. **Blender version** (e.g. 5.0.1)
2. **OS and architecture** (e.g. Windows 11 x64)
3. **Controller model** (e.g. Xbox Series X, DualSense, generic USB gamepad)
4. **Pygame version** (`pip show pygame` inside Blender's Python)
5. **Steps to reproduce** — what you did, what you expected, what happened
6. **Error output** from the Blender system console (Window → Toggle System Console on Windows)

---

## Adding a New Mode

Modes live in `modes/` and follow a simple interface:

1. **Create `modes/your_mode.py`** with at minimum:
   - A `tick(context, input_state)` function that receives the current normalized input and applies viewport/camera changes.
   - Any mode-specific settings documented as comments or a `DEFAULTS` dict.
2. **Register the mode** in `core/state.py` by adding it to the mode registry.
3. **Expose the mode switcher** in `ui/panel.py` — add an enum entry and the relevant sensitivity controls.
4. **Update `README.md`** to document the new mode and its controller reference.

---

## Adding Controller Bindings

All button and axis mappings live in `core/mapping.py` as the single source of truth. To remap or add bindings:

1. Add or modify the relevant constant in `mapping.py`.
2. Update `core/input_manager.py` if the new input requires different normalization (e.g. a trigger axis vs. a thumbstick).
3. Document the new binding in the **Controller Reference** table in `README.md`.

---

## License

By contributing, you agree that your contributions will be licensed under the [GPL-3.0 License](LICENSE) that covers this project.

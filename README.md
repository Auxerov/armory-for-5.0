# armory (Blender 5.0+ Compatible)

[Download](https://armory3d.org/engine/download) &bullet; [Release Notes](https://github.com/armory3d/armory/releases) &bullet; [Manual](https://github.com/armory3d/armory/wiki) &bullet; [Forums](https://forums.armory3d.org/)

Armory is an open-source 3D game engine focused on portability, minimal footprint and performance. The renderer is fully scriptable with deferred and forward paths supported out of the box.

Armory as a Blender add-on provides a full Blender integration, turning it into a complete game development tool and a unified workflow from start to finish.

![](http://armory3d.org/git/img1.jpg)

## Blender 5.0+ Compatibility & Fixes

This fork is patched and optimized for **Blender 5.0+**:
- **`bgl` compatibility shim**: Built-in OpenGL compatibility shim for Blender 4.0+ and 5.0+ where `bgl` was removed.
- **Cycles Shader Nodes**: Updated shader converters and texture parsers for nodes deprecated or removed in Blender 5.0 (Combine/Separate HSV/RGB, PointDensity).
- **Modern Blender API Fixes**: Fixed `blf.size()` signature for Blender 4.1+/5.0+, empty PropertyGroup syntax, and Cycles tile size configuration.
- **Addon Loader & Auto-detection**: Includes root `__init__.py` and intelligent SDK path detection so it can be installed directly from GitHub ZIP or cloned as a folder without manual setup.

### How to Install in Blender 5.0

1. **Download:**
   - Click `<> Code` -> **Download ZIP** on GitHub (or clone this repository).
2. **Install Add-on in Blender:**
   - Open Blender 5.0, go to **Edit** -> **Preferences** -> **Add-ons**.
   - Click the top right menu -> **Install from Disk...**
   - Select the downloaded `.zip` file (or select `armory.py`).
   - Search for **Armory** and enable the add-on.
3. **SDK Path:**
   - The add-on will automatically detect its SDK path. If needed, you can set the SDK path in the Armory preferences or via the `ARMSDK` environment variable.


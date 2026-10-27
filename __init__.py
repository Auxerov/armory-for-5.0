# Armory 3D Engine - Blender 5.0+ Compatible
bl_info = {
    "name": "Armory",
    "category": "Render",
    "location": "Properties -> Render -> Armory Player",
    "description": "3D Game Engine for Blender (Blender 5.0+ Compatible)",
    "author": "Armory3D.org",
    "version": (2026, 2, 0),
    "blender": (4, 2, 0),
    "doc_url": "https://github.com/armory3d/armory/wiki",
    "tracker_url": "https://github.com/Auxerov/armory-for-5.0/issues"
}

import importlib.util
import os
import sys

_armory_file = os.path.join(os.path.dirname(__file__), "armory.py")
_spec = importlib.util.spec_from_file_location("armory", _armory_file)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["armory"] = _mod
_spec.loader.exec_module(_mod)


def register():
    _mod.register()


def unregister():
    _mod.unregister()


if __name__ == "__main__":
    register()

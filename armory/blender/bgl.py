# Compatibility shim for bgl (removed in Blender 4.0+)
# Provides OpenGL constants, Buffer class, and stubs/fallbacks for legacy Armory calls.

GL_BLEND = 0x0BE2
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE_2D = 0x0DE1
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_BACK = 0x0405
GL_FRONT = 0x0404
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_RGBA = 0x1908
GL_RGB = 0x1907
GL_DEPTH_COMPONENT = 0x1902

def glEnable(cap):
    pass

def glDisable(cap):
    pass

def glActiveTexture(texture):
    pass

def glBindTexture(target, texture):
    pass

def glReadBuffer(mode):
    pass

def glReadPixels(x, y, width, height, format, type, buffer):
    pass

class Buffer:
    def __init__(self, type, dimensions):
        self.type = type
        if isinstance(dimensions, int):
            self.dimensions = (dimensions,)
            self._data = [0] * dimensions
        elif isinstance(dimensions, (list, tuple)):
            self.dimensions = tuple(dimensions)
            total = 1
            for d in dimensions:
                total *= d
            self._data = [0] * total
        else:
            self._data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def to_list(self):
        return list(self._data)

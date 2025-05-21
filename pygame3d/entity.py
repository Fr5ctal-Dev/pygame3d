class Entity:
    """
    Basic wrapper for Panda3D classes
    """
    def __init__(self, panda_object):
        self.core = panda_object

    @property
    def position(self):
        return self.core.get_pos()

    @position.setter
    def position(self, position):
        self.core.set_pos(position)

    @property
    def rotation(self):
        return self.core.get_hpr()

    @rotation.setter
    def rotation(self, rotation):
        self.core.set_hpr(rotation)

    @property
    def scale(self):
        return self.core.get_scale()

    @scale.setter
    def scale(self, scale):
        self.core.set_scale(scale)

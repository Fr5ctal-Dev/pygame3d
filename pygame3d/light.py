from pygame3d.entity import Entity
from panda3d.core import PointLight, DirectionalLight, AmbientLight, NodePath
from typing import Literal


class Light(Entity):
    """
    Light class for lights and illumination in the 3D surface
    """
    def __init__(self, type: Literal['point', 'directional', 'ambient']):
        if type == 'point':
            light = PointLight('plight')
        elif type == 'directional':
            light = DirectionalLight('dlight')
        elif type == 'ambient':
            light = AmbientLight('ablight')
        else:
            raise Exception(f'Invalid light type: {type}')

        light = NodePath(light)
        super().__init__(light)

    @property
    def color(self):
        return self.core.node().get_color()

    @color.setter
    def color(self, color: tuple):
        self.core.node().set_color(color)

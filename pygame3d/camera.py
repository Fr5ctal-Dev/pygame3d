from pygame3d.entity import Entity
from panda3d.core import Camera as _Camera, NodePath


class Camera(Entity):
    """
    Camera class for controlling the main camera in the surface
    """
    def __init__(self):
        camera = NodePath(_Camera('camera'))
        super().__init__(camera)

    @property
    def fov(self):
        return self.core.node().get_lens().get_fov()

    @fov.setter
    def fov(self, fov):
        self.core.node().get_lens().set_fov(fov)

    @property
    def aspect_ratio(self):
        return self.core.node().get_lens().get_aspect_ratio()

    @aspect_ratio.setter
    def aspect_ratio(self, ratio):
        self.core.node().get_lens().set_aspect_ratio(ratio)

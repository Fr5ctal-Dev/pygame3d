from pygame3d.entity import Entity
from direct.showbase.Loader import Loader


class Mesh(Entity):
    """
    Mesh class for loading 3D models into surface
    """
    def __init__(self, file: str):
        mesh = Loader(None).load_model(file)
        super().__init__(mesh)

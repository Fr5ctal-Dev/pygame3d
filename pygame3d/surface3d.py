from pygame3d.camera import Camera
from pygame3d.mesh import Mesh
import pygame
from panda3d.core import (GraphicsOutput,
                          Texture,
                          GraphicsEngine,
                          GraphicsPipe,
                          GraphicsPipeSelection,
                          FrameBufferProperties,
                          WindowProperties,
                          NodePath,
                          PerspectiveLens,
                          AmbientLight)


class Surface3D(pygame.Surface):
    """
    The main class for 3D rendering in pygame onto a pygame surface
    Args:
        - Pygame surface arguments
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._graphics_engine = GraphicsEngine()
        self._graphics_pipe = GraphicsPipeSelection.get_global_ptr().make_default_pipe()

        fb_props = FrameBufferProperties()
        fb_props.set_rgb_color(True)
        fb_props.set_alpha_bits(8)
        fb_props.set_depth_bits(24)

        win_props = WindowProperties()
        win_props.setSize(*self.get_size())

        flags = (
                GraphicsPipe.BF_refuse_window |
                GraphicsPipe.BF_can_bind_every |
                GraphicsPipe.BF_rtt_cumulative
        )

        self._graphics_buffer = self._graphics_engine.make_output(
            self._graphics_pipe,
            'offscreen-buffer',
            -2,
            fb_props,
            win_props,
            flags,
            None
        )

        self._graphics_texture = Texture()
        self._graphics_buffer.add_render_texture(self._graphics_texture, GraphicsOutput.RTM_copy_ram)

        self._root_node = NodePath('root')

        self.camera = Camera()
        self.camera.core.reparent_to(self._root_node)
        self.camera.core.node().set_lens(PerspectiveLens())
        self.camera.core.node().get_lens().set_aspect_ratio(self.get_width() / self.get_height())

        self._display_region = self._graphics_buffer.make_display_region()
        self._display_region.camera = self.camera.core
        self._display_region.set_clear_color_active(True)
        self._display_region.set_clear_color((0, 0, 0, 0))

    def render(self) -> None:
        """
        Renders the surface in-place.
        Needs to be called once every frame or before being blit onto another surface.
        """
        self._graphics_engine.render_frame()
        if not self._graphics_texture.has_ram_image():
            return

        tex_data = self._graphics_texture.get_ram_image_as('RGB')
        image_data = tex_data.get_data()

        surface = pygame.image.fromstring(image_data, [self._graphics_texture.get_x_size(), self._graphics_texture.get_y_size()], 'RGB', True)

        self.blit(surface, (0, 0))

    def load_mesh(self, file: str) -> Mesh:
        """
        Loads given mesh file into surface.
        Returns Mesh object
        Args:
            - Filename

        For more information on 3D mesh loading, check out Panda3d's docs at https://docs.panda3d.org/
        """
        try:
            mesh = Mesh(file)
        except:
            raise Exception('Mesh file is not supported or invalid')

        mesh.core.reparent_to(self._root_node)
        return mesh

    @property
    def background_color(self):
        return self._display_region.get_clear_color()

    @background_color.setter
    def background_color(self, color):
        self._display_region.set_clear_color((*color[:3], 0))

# Basic model loading and rendering

import pygame
import pygame3d
import sys

# Initialize the pygame library
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a 3D surface
surface = pygame3d.Surface3D((800, 600))

# Configure background color
surface.background_color = (255, 255, 255) # White

# Loading a model
model = surface.load_mesh('assets/avocado.glb')
model.position = (0, 20, -2)
model.rotation = (50, 0, 0)
model.scale = 100

# Add a light
light = surface.add_light('ambient')
light.color = (150, 150, 150)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.render() # Render the surface to display the newest updates
    screen.blit(surface, (0, 0))

    pygame.display.update()
    clock.tick(60) # 60 FPS

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
surface.background_color = (145, 216, 255) # Sky blue

# Loading a model
model = surface.load_mesh('assets/model.glb')
model.position = (0, 20, -2)

# Add a light
light = surface.add_light('point')
light.position = (20, 20, 20)

# Main game loop
while True:
    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    model.rotation += (1, 0, 0) # Rotate the model
    surface.render() # Render the surface to display the newest updates
    screen.blit(surface, (0, 0))

    pygame.display.update()
    clock.tick(60) # 60 FPS

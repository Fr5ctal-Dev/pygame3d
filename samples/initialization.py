# Initialization.py for basic setup of pygame3d with pygame

import pygame
import pygame3d
import sys

# Initialize the pygame library
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a 3D surface
surface = pygame3d.Surface3D((600, 400))

# Main game loop
while True:
    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.render() # Render the surface to display the newest updates
    screen.blit(surface, (0, 0))

    pygame.display.update()
    clock.tick(60) # 60 FPS

# Pygame 3D
Pygame3D is a cross-platform open-source python library for basic 3D rendering in [PyGame](https://www.pygame.org/). It has many features, from 3D rendering to camera control. It is extremely simple, with a streamlined creation process, and just like what its name suggests, it integrates perfectly into PyGame.

### Results
______
Scene rendering:
![](assets/screenshot1.png)

## Installation

----------
To install Pygame3D, use the Python Package Manager and type:
```
pip install pygame3d
```

Once it is installed, you can start using it just like any other module!

## Documentation

-------
To learn more about this module, you can read its documentation [here](https://github.com/Fr5ctal-Projects/pygame3d/wiki)

## Quickstart

------
Here is a sample code to render a 3D model in Pygame3D, as shown in the image above.
```python
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

light2 = surface.add_light('ambient')
light2.color = (50, 50, 50)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    model.rotation += (1, 0, 0) # Rotate the model
    surface.render() # Render the surface to display the newest updates
    screen.blit(surface, (0, 0))

    pygame.display.update()
    clock.tick(60) # 60 FPS

```

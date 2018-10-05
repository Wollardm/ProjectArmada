"""
    Should probably make a real docstring. Oh well.
"""

import pygame
from technode import TechNode
from utils import vec3


WIDTH = 1200
HEIGHT = 800

root_nodes = set()
camera_pos = vec3(0, 0, 1)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if event.button == 1:
                root_nodes.add(TechNode(mousepos[0], mousepos[1]))
        elif event.type == pygame.KEYDOWN:
            pass

    # TODO: Change to move with delta time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_pos += (0, -1, 0)
    if keys[pygame.K_a]:
        camera_pos += (-1, 0, 0)
    if keys[pygame.K_s]:
        camera_pos += (0, 1, 0)
    if keys[pygame.K_d]:
        camera_pos += (1, 0, 0)

    screen.fill((0, 0, 0))
    for node in root_nodes:
        node.render(screen, camera_pos)

    pygame.display.flip()

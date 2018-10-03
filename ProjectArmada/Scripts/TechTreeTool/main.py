"""
    Should probably make a real docstring. Oh well.
"""

import pygame
from technode import TechNode


WIDTH = 1200
HEIGHT = 800

root_nodes = set()

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
            left, mid, right = pygame.mouse.get_pressed()
            mousepos = pygame.mouse.get_pos()
            print(mousepos[0])

            if left:
                root_nodes.add(TechNode(mousepos[0], mousepos[1]))

    screen.fill((0, 0, 0))
    for node in root_nodes:
        node.render(screen)

    pygame.display.flip()

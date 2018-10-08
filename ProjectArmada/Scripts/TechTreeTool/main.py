"""
    Should probably make a real docstring. Oh well.
"""

import pygame
from technode import *
from utils import vec3


WIDTH = 1200
HEIGHT = 800

nodes = set()
selected_node = None
start_node = None
end_node = None
camera_pos = vec3(0, 0, 1)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    mousepos = vec3(pygame.mouse.get_pos()) + camera_pos

    # Handle input, etc
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not check_create_collision(nodes, mousepos):
                    nodes.add(TechNode(mousepos[0], mousepos[1]))
                else:
                    selected_node = select_node_at(nodes, mousepos)
            elif event.button == 3:
                start_node = select_node_at(nodes, mousepos)

        elif event.type == pygame.MOUSEBUTTONUP:
            mousepos = vec3(pygame.mouse.get_pos()) + camera_pos
            # Add the connections
            if event.button == 3:
                end_node = select_node_at(nodes, mousepos)
                if start_node and end_node:
                    start_node.connections.add(end_node)
                    end_node.dependencies.add(start_node)

                start_node = None
                end_node = None

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

    # Rendering
    screen.fill((0, 0, 0))
    for node in nodes:
        node.render(screen, camera_pos)

    if start_node and not end_node:
        pygame.draw.line(screen, (0, 0, 255),
                         (start_node.pos - camera_pos).to2ituple(),
                         (mousepos - camera_pos).to2ituple())

    pygame.display.flip()

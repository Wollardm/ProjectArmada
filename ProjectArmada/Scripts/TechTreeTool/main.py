"""
Should probably make a real docstring. Oh well.

TODOLIST:
[x] TODO: Change camera to move with delta time
[x] TODO: Create links to other nodes
[ ] TODO: Ability to select node and edit
[ ] TODO: Add Name
[ ] TODO: Add Description
[ ] TODO: Add Costs
[ ] TODO: Add Modifiers
[ ] TODO: Add Icons
[ ] TODO: Write to file
[ ] TODO: Render Icon
[ ] TODO: Display gris/axes
[ ] TODO: Implement axis snap
[ ] TODO: D O C S T R I N G S
"""

import pygame
from technode import *
from utils import vec3


WIDTH = 1200
HEIGHT = 800
CAM_SPEED = 600

nodes = set()
selected_node = None
start_node = None
end_node = None
camera_pos = vec3(0, 0, 1)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick()

running = True
while running:
    deltatime = clock.tick() / 1000.0
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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_pos += (0, -CAM_SPEED * deltatime, 0)
    if keys[pygame.K_a]:
        camera_pos += (-CAM_SPEED * deltatime, 0, 0)
    if keys[pygame.K_s]:
        camera_pos += (0, CAM_SPEED * deltatime, 0)
    if keys[pygame.K_d]:
        camera_pos += (CAM_SPEED * deltatime, 0, 0)

    # Rendering
    screen.fill((0, 0, 0))
    for node in nodes:
        node.render(screen, camera_pos)

    if start_node and not end_node:
        pygame.draw.line(screen, (0, 0, 255),
                         (start_node.pos - camera_pos).to2ituple(),
                         (mousepos - camera_pos).to2ituple())

    pygame.display.flip()

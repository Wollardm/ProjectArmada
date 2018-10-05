"""
    Something Something.
    # TODO: Create links to other nodes
    # TODO: Add Name
    # TODO: Add Description
    # TODO: Add Modifiers
    # TODO: Add Icons
    # TODO: Render Icon
    # TODO: Write to file
"""
import pygame
from utils import vec3

class TechNode:
    """
        Putting this so pylint doesn't bitch at me.
    """

    node_count = 0

    def __init__(self, x, y):
        """
            Do init funcs even require docstrings? Iunno.
        """
        self.ID = TechNode.node_count
        TechNode.node_count += 1
        self.name = ""
        self.dec = ""
        self.pos = vec3(x, y, 1)
        self.selected = False
        self.type = "Something"
        self.connections = []
        self.dependencies = []

    def write_to_file(self, filename):
        """
            Also doing this to avoid bitching.
        """
        pass

    # TODO: Make render use node icon
    def render(self, screen, cam_pos):
        """
            Eventually get this to display a the node art maybe?.
        """
        new_pos = self.pos - cam_pos
        pygame.draw.circle(screen, (255, 0, 0), (new_pos.to2ituple()), 20)

"""
    Something Something.
"""
import pygame
from utils import vec2

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
        self.pos = vec2(x, y)
        self.selected = False
        self.type = "Something"
        self.connections = []
        self.dependencies = []

    def write_to_file(self, filename):
        """
            Also doing this to avoid bitching.
        """
        pass

    def render(self, screen):
        """
            Eventually get this to display a the node art maybe?.
        """
        pygame.draw.circle(screen, (255, 0, 0), self.pos.toituple(), 20)

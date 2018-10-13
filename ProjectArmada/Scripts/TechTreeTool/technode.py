"""
Something Something.
"""
import pygame
from utils import vec3, length


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
        self.name = "None"
        self.dec = "None."
        self.mods = []
        self.techs = []
        self.type = "None"
        self.flavor = "None.\n-Nobody"
        self.pos = vec3(x, y, 1)
        self.radius = 20
        self.selected = False
        self.connections = set()
        self.dependencies = set()
        self.color = (255, 0, 0)

    def write_to_file(self, filename):
        """Also doing this to avoid bitching.

        Args:
        Returns:
        Raises:
        """
        pass

    def render(self, screen, cam_pos):
        """Draws the node.

        Renders the node onto the screen & any connections it has with other
        nodes. Must translate from world space to screen space using the
        camera's position.

        TODO: Get this to display a the node art maybe?

        Args:
            screen (pygame.Surface): The surface to draw the node onto.
            cam_pos (vec3): The position of the camera in the world.
        Returns:
            Nothing.
        Raises:
            Nothing.
        """
        new_pos = self.pos - cam_pos
        pygame.draw.circle(screen, self.color, (new_pos.to2ituple()),
                           self.radius)
        for node in self.connections:
            pygame.draw.line(screen, self.color, new_pos.to2ituple(),
                             (node.pos - cam_pos).to2ituple())


def check_collision(node, mousepos, pad=0):
    """Node & Mouse collision.

    Checks if there will be a collision with the given node and the
    given position.

    Args:
        node (TechNode): The node to check against.
        mousepos (vec3): The point to check against.
        pad (int): Added to diameter for extra distance.
    Returns:
        bool: True if collision, False if not.
    Raises:
        AssertionError: If mousepos is not a vec3.
    """
    assert isinstance(mousepos, vec3)
    dist = length(node.pos - mousepos)
    if dist < node.radius * 2 + pad:
        return True
    return False

def check_create_collision(nodes, mousepos):
    """Node creation collision.

    Checks if there will be a collision with the node created at the
    current position and any other node.

    Args:
        nodes (list): List of all nodes.
        mousepos (vec3): The point to check against.
    Returns:
        bool: True if collision, False if not.
    Raises:
        AssertionError: If mousepos is not a vec3.
    """
    assert isinstance(mousepos, vec3)
    for node in nodes:
        if check_collision(node, mousepos, 5):
            return True
    return False

def select_node_at(nodes, mousepos):
    """Selected the node at the given position, if any.

    Args:
        nodes (list): List of all nodes
        mousepos (vec3): The point to check against
    Returns:
        TechNode: The node at the given position, None if no node.
    Raises:
        AssertionError: If mousepos is not a vec3.
    """
    assert isinstance(mousepos, vec3)
    for node in nodes:
        if check_collision(node, mousepos):
            return node
    return None

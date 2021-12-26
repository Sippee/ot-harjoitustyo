"""Presents a game window
"""

import pygame

class Window:
    """A class used to present the game window for the game.
    """
    def __init__(self, width, height):
        """Constructor of the class, which handles the properties of the game window.

        Args:
            coin:
                width: Width of the window
                height: Height of the window
        """

        self.width = width
        self.height = height
        self.game_window = pygame.display.set_mode((self.width,self.height))

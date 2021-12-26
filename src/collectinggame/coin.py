"""Presents a collectable coin in the game.
"""

import pygame

class Coin:
    """A class used to present the coin in the game.
    The collector collects these in the game.
    """
    def __init__(self,x_coordinate,y_coordinate,window):
        """Constructor of the class, which handles the properties of the coin.

        Args:
            coin:
                x: x coordinate of the coin
                y: y coordinate of the coin
                window: Window-object. Window which the coin is part of.
        """

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.height = 20
        self.width = 20
        self.coinimage = pygame.image.load('src/collectinggame/images/coinv2.png')
        self.window = window

    def draw(self):
        """Draws the coin
        """

        self.rect = self.window.game_window.blit(self.coinimage,
        (self.x_coordinate, self.y_coordinate))

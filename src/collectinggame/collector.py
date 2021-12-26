"""Presents the playable character in the game.
"""

import pygame

class Collector:
    """A class used to present the collector in the game.
    The collector is the character that player moves in the game.
    """
    def __init__(self,x_coordinate,y_coordinate,window):
        """Constructor of the class, which handles the properties of the collector.

        Args:
            coin:
                x: x coordinate of the coin
                y: y coordinate of the coin
                window: Window-object. Window which the collector is part of.
        """

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.width = 40
        self.height = 40
        self.speed = 5
        self.collectorimage = pygame.image.load(
            'src/collectinggame/images/coincollector.png')
        self.window = window

    def draw(self):
        """Draws the player controlled collector
        """

        self.rect = self.window.game_window.blit(self.collectorimage,
        (self.x_coordinate, self.y_coordinate))

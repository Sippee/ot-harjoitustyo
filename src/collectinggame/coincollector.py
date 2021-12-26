"""Contains the logic of the game
"""

from random import randint
import pygame
from collectinggame.coin import Coin
from collectinggame.collector import Collector
from collectinggame.window import Window

def main_game(game_length):
    """This method hold the game logic.

    Args:
        game_length: Optional, Length of the game, 30000 means 30 seconds.

    Returns:
        Score: How many coins the player collected within one game.
    """

    # Initiating the game and setting the title for the window
    pygame.init()
    pygame.display.set_caption("Coin Collector")

    # Creating the window for the game
    game_window = Window(500,500)
    game_width = game_window.width
    game_height = game_window.height
    window = game_window.game_window

    # Refreshrate of the game
    refreshrate = 60
    clock = pygame.time.Clock()

    # The objects of the game
    # Player controls the collector
    # Coin is collected by the collector
    collector = Collector(160,160, game_window)
    coin = Coin(randint(20, game_width-20), randint(20, game_height-20), game_window)

    # The score displayy
    font = pygame.font.Font('freesansbold.ttf', 26)
    score = 0
    scoretext = font.render('Score = ' + str(score), True, (255,255,255))
    scoretextrectangle = scoretext.get_rect()
    scoretextrectangle.topleft = (20, 20)

    # The time left display
    time = pygame.time.get_ticks()/1000
    timetext = font.render('Time left = ' + str(time), True, (255,255,255))
    timetextrectangle = timetext.get_rect()
    timetextrectangle.topleft = (20, 50)


    # Main game loop
    runningisgame = True
    while pygame.time.get_ticks() < game_length and runningisgame is True:
        clock.tick(refreshrate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningisgame = False


    # Fill the window, draw objects and texts
        window.fill((0,0,0))
        window.blit(scoretext,scoretextrectangle)
        window.blit(timetext,timetextrectangle)

        collector.draw()
        coin.draw()

    # Player movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and collector.x_coordinate > 0:
            collector.x_coordinate -= collector.speed

        if keys[pygame.K_RIGHT] and collector.x_coordinate < game_width-40:
            collector.x_coordinate += collector.speed

        if keys[pygame.K_DOWN] and collector.y_coordinate < game_height-40:
            collector.y_coordinate += collector.speed

        if keys[pygame.K_UP] and collector.y_coordinate > 0:
            collector.y_coordinate -= collector.speed

    # Player collects a coin, get a score,
    # score display updates and the coin gets moved to random location
        if collector.rect.colliderect(coin.rect):
            score += 1
            collector.speed+=0.5

            coin = Coin(randint(20, game_width-20), randint(20, game_height-20), game_window)

            scoretext = font.render('Score = ' + str(score), True, (255,255,255))
            scoretextrectangle = scoretext.get_rect()
            scoretextrectangle.topleft = (20, 20)

    # Time left display updates
        time = int(30-pygame.time.get_ticks()/1000)
        timetext = font.render('Time left = ' + str(time), True, (255,255,255))
        timetextrectangle = timetext.get_rect()
        timetextrectangle.topleft = (20, 50)

        pygame.display.update()

    # Window closes and returns the score
    pygame.quit()
    return score

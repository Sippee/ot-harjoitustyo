import pygame
from random import randint

#coin class
class Coin:
    def __init__(self,x,y,window):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 20
        self.coinImg = pygame.image.load('src/collectinggame/images/coinv2.png')
        self.window = window
    def draw(self):
        self.rect = self.window.game_window.blit(self.coinImg, (self.x, self.y))

#collector class
class Collector:
    def __init__(self,x,y,window):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 5
        self.collectorImg = pygame.image.load('src/collectinggame/images/coincollector.png')
        self.window = window
    def draw(self):
        self.rect = self.window.game_window.blit(self.collectorImg, (self.x, self.y))

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_window = pygame.display.set_mode((self.width,self.height))

def main_game():
    pygame.init()
    pygame.display.set_caption("Coin Collector")

    game_window = Window(500,500)
    game_width = game_window.width
    game_height = game_window.height
    window = game_window.game_window

    #window refreshrate
    FPS = 60
    clock = pygame.time.Clock()


    collector = Collector(160,160, game_window)
    coin = Coin(randint(20, game_width-20), randint(20, game_height-20), game_window)

    #score display
    font = pygame.font.Font('freesansbold.ttf', 26)
    score = 0
    scoretext = font.render('Score = ' + str(score), True, (255,255,255))
    scoretextRect = scoretext.get_rect()  
    scoretextRect.topleft = (20, 20)

    #time display
    time = pygame.time.get_ticks()/1000
    timetext = font.render('Time left = ' + str(time), True, (255,255,255))
    timetextRect = timetext.get_rect()  
    timetextRect.topleft = (20, 50)


    #main
    runninggame = True
    while pygame.time.get_ticks() < 30000 and runninggame == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runninggame = False


    #draw window and objects
        window.fill((0,0,0))
        window.blit(scoretext,scoretextRect)
        window.blit(timetext,timetextRect)

        collector.draw()
        coin.draw()

    #movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and collector.x > 0:
            collector.x -= collector.speed

        if keys[pygame.K_RIGHT] and collector.x < game_width-40:
            collector.x += collector.speed

        if keys[pygame.K_DOWN] and collector.y < game_height-40:
            collector.y += collector.speed

        if keys[pygame.K_UP] and collector.y > 0:
            collector.y -= collector.speed

    #player collects a coin and get a score, scoretext updates
        if collector.rect.colliderect(coin.rect):
            score += 1
            collector.speed+=0.5

            coin = Coin(randint(20, game_width-20), randint(20, game_height-20), game_window)

            scoretext = font.render('Score = ' + str(score), True, (255,255,255))
            scoretextRect = scoretext.get_rect()  
            scoretextRect.topleft = (20, 20)    

    #time left text updates
        time = int(30-pygame.time.get_ticks()/1000)
        timetext = font.render('Time left = ' + str(time), True, (255,255,255))
        timetextRect = timetext.get_rect()  
        timetextRect.topleft = (20, 50)

        pygame.display.update()
    pygame.quit()
    return score

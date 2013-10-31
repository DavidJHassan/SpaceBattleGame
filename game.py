#!/usr/bin/python
__author__ = 'david'

from pygame import *
from Battlecruiser import *
from Enemy import *
from sys import exit


pygame.init()
#Global Variables

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
screenT = [screen, screen_size[0], screen_size[1]]

try:
    uranus_image = pygame.image.load("assets/ram_aras.png")
except ImportError:
    print "Failed to load ram_aras.png"

black = (0, 0, 0)

cruiser = Battlecruiser(screenT,[400, 400])
enemylist = []

for i in range(0,10):
    enemylist.append(Enemy(screenT,[350,5], cruiser))

clock = pygame.time.Clock()


# The event loop.
running = True
while running:

    #Make sure the game runs at 50 FPS
    time_passed = clock.tick(50)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cruiser.moveX(-2)
    elif keys[pygame.K_RIGHT]:
         cruiser.moveX(2)
    else:
        cruiser.moveX(0)

    if keys[pygame.K_UP]:
        cruiser.moveY(-2)
    elif keys[pygame.K_DOWN]:
        cruiser.moveY(2)
    else:
        cruiser.moveY(0)

    if event.type == pygame.KEYDOWN:

        if keys[pygame.K_SPACE]:
            cruiser.laser_fired()

        if keys[pygame.K_ESCAPE]:
            exit(0)

    font = pygame.font.Font(None, 16)
    screen.fill(black)
    screen.blit(uranus_image, [0,0])
    cruiser.draw()
    cruiser.update()

    score = 0
    for e in enemylist:
        e.draw()
        e.update()
        dead_list = []
        if not e.is_active():
            dead_list.append(e)
        score = score + len(dead_list)*100

    font = pygame.font.Font(None, 50)
    text_pos = (0, 0)
    text_surface = font.render('Score: '+str(score), 50, (255,255,255))
    screen.blit(text_surface, text_pos)

    if not cruiser.is_active():
        font = pygame.font.Font(None, 200)
        text_pos = (0, 200)
        text_surface = font.render('Game Over', 200, (255,255,255))
        screen.blit(text_surface, text_pos)
    if score == 1000:
        font = pygame.font.Font(None, 200)
        text_pos = (100, 200)
        text_surface = font.render('You Win', 200, (255,255,255))
        screen.blit(text_surface, text_pos)

    pygame.display.flip()
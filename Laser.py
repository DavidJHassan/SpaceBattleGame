#!/usr/bin/python
__author__ = 'david'
import pygame

class Laser(pygame.sprite.Sprite):
    image = None
    x = 0
    y = 0
    dx = 0
    dy = 0
    screen = None
    image_w = None
    image_h = None
    active = False
    rect = None

    def __init__(self, screen, location):
        pygame.sprite.Sprite.__init__(self)
        if Laser.image is None:
            # This is the first time this class has been
            # instantiated. So, load the image for this and
            # all subsequence instances.
            try:
                Laser.image = pygame.image.load("assets/laser.gif")
            except ImportError:
                print "Failed to load laser.gif "

        self.screen = screen
        self.x = location[0]
        self.y = location[1]
        self.dx = 0
        self.dy = -5

        self.image = Laser.image
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()


        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

        self.active = True

    def draw(self):
        self.screen.blit(self.image, [self.x,self.y])


    def update(self):
        self.x = self.x+self.dx
        self.y = self.y+self.dy
        self.update_rect()

    def getX(self):
        return self.x

    def update_rect(self):
        self.rect.topleft = [self.x,self.y]

    def getY(self):
        return self.y

    def getRect(self):
        return self.rect

if __name__ == "__main__":
    from pygame import *
    from sys import exit
    import random
    import time


    pygame.init()

    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    screenT = [screen, screen_size[0], screen_size[1]]


    black = (0, 0, 0)


    laserlist = []
    for i in range(0,50):
        random.seed(time.time())
        x = random.uniform(0, screen_size[0])
        y = random.uniform(0, screen_size[1])
        laserlist.append(Laser(screen,[x,y]))

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

        if event.type == pygame.KEYDOWN:

            if keys[pygame.K_ESCAPE]:
                exit(0)


        screen.fill(black)

        for i in range(0,1):
            random.seed(time.time())
            x = random.uniform(0, screen_size[0])
            y = random.uniform(0, screen_size[1])
            laserlist.append(Laser(screen,[x,y]))

        for l in laserlist:
            if l.getY() < 0:
                laserlist.remove(l)
            else:
                l.update()
                l.draw()

        pygame.display.flip()

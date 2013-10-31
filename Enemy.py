#!/usr/bin/python
__author__ = 'david'
import pygame
from Laser import *
import random
import time

class Enemy(pygame.sprite.Sprite):
    image = None
    x = 0
    y = 0
    dx = 0
    dy = 0
    screen = None
    screen_x = 0
    screen_y = 0
    image_w = None
    image_h = None
    active = False
    rect = None

    def __init__(self, screen, location, otherPlayer):
        pygame.sprite.Sprite.__init__(self)
        if Enemy.image is None:
            # This is the first time this class has been
            # instantiated. So, load the image for this and
            # all subsequence instances.
            try:
                Enemy.image = pygame.image.load("assets/mutalisk.gif")
            except ImportError:
                print "Failed to load mutalisk.gif.gif "

        try:
            self.explosion_image = pygame.image.load("assets/laser_explosion.gif")
        except ImportError:
             print "Failed to load laser_explosion.gif "

        try:
            self.explosion_sound = pygame.mixer.Sound("assets/death_explode.wav")
            self.explosion_sound.set_volume(0.1)

        except ImportError:
            print "Failed to load death_explode.wav"

        self.player = otherPlayer
        self.screen = screen[0]
        self.screen_x = screen[1]
        self.screen_y = screen[2]
        self.x = location[0]
        self.y = location[1]

        random.seed(time.time())
        self.dx = random.uniform(0, 2)
        self.dy = random.uniform(0, 2)

        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

        self.active = True

    def draw(self):
        if self.active:
            self.screen.blit(self.image, [self.x,self.y])
        else:
            self.screen.blit(self.explosion_image, [self.x, self.y])

    def update(self):
        if self.active:
            if self.x <= 0 or self.x >= self.screen_x - self.image_w:
                self.dx = -self.dx

            if self.y <= 0 or self.y >=  self.screen_y - self.image_h:
                  self.dy = -self.dy


            self.x = self.x+self.dx
            self.y = self.y+self.dy

            self.update_rect()
            self.check_collision()

    def update_rect(self):
        self.rect.topleft = [self.x,self.y]


    def check_collision(self):
        rect = self.player.getRect()
        lasers = self.player.get_lasers()

        if self.rect.colliderect(rect) and self.player.is_active():
            self.player.dead()
            self.active = False
            self.explosion_sound.play(0)

        for l in lasers:
            if self.rect.colliderect(l.getRect()):
                self.active = False
                self.player.remove_a_laser(l)
                self.explosion_sound.play(0)

    def is_active(self):
        return self.active

if __name__ == "__main__":
    from pygame import *
    from Battlecruiser import *
    from sys import exit
    import random
    import time

    pygame.init()

    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    screenT = [screen, screen_size[0], screen_size[1]]

    white = (255, 255, 255)

    cruiser = Battlecruiser(screenT,[-400, -400])#Position off screen. Needed for Enemy constructor
    enemylist = []

    for i in range(0,10):
        enemylist.append(Enemy(screenT,[400,50],cruiser))

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

        screen.fill(white)

        for e in enemylist:
            e.update()
            e.draw()

        pygame.display.flip()

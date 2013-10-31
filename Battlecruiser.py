#!/usr/bin/python
__author__ = 'david'
import pygame
from Laser import *

class Battlecruiser(pygame.sprite.Sprite):
    image = None
    explosion_image = None
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
    laserlist = []


    def __init__(self, screen, location):
        pygame.sprite.Sprite.__init__(self)
        if Battlecruiser.image is None:
            # This is the first time this class has been
            # instantiated. So, load the image for this and
            # all subsequence instances.
            try:
                Battlecruiser.image = pygame.image.load("assets/battlecruiser.gif")
            except ImportError:
                print "Failed to load Battlecruiser.gif "
        if self.explosion_image is None:

            try:
                self.explosion_image = pygame.image.load("assets/laser_explosion.gif")
            except ImportError:
                 print "Failed to load laser_explosion.gif "


        try:
            self.laser_sound = pygame.mixer.Sound("assets/laser.wav")
            self.laser_sound.set_volume(0.3)
        except ImportError:
            print "Failed to load laser.wav"


        self.explosion = self.explosion_image

        self.screen = screen[0]
        self.screen_x = screen[1]
        self.screen_y = screen[2]
        self.x = location[0]
        self.y = location[1]
        self.dx = 0
        self.dy = 0

        self.moving_x = False
        self.moving_y = False

        self.image = Battlecruiser.image
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()


        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

        self.active = True

    def draw(self):
        if self.active:
            self.screen.blit(self.image, [self.x,self.y])
        else:
            self.screen.blit(self.explosion_image, [self.x,self.y])
        self.draw_laser()


    def getRect(self):
        return self.rect


    def moveX(self,dx):
        self.dx = dx

    def moveY(self,dy):
        self.dy = dy

    def dead(self):
        self.active = False

    def update(self):
        if self.active:
            x = self.x + self.dx
            if x != 0 and x != self.screen_x-self.image_w:
                self.x = self.x+self.dx

            y = self.y + self.dy
            if y != 0 and y != self.screen_y-self.image_h:
                self.y = self.y+self.dy

            self.update_rect()
        self.remove_laser()
        self.update_laser()


    def update_rect(self):
        self.rect.topleft = [self.x,self.y]

    def draw_laser(self):
        for l in self.laserlist:
            l.draw()

    def update_laser(self):
         for l in self.laserlist:
            l.update()

    def remove_laser(self):
        #If laser is offscreen
        for l in self.laserlist:
            if l.getY() < 0:
                self.laserlist.remove(l)

    def remove_a_laser(self,laser):
        self.laserlist.remove(laser)


    def laser_fired(self):
        if self.active:
            laser = Laser(self.screen,[self.x+self.image_w/2,self.y])
            self.laserlist.append(laser)
            self.laser_sound.play(0)

    def is_active(self):
        return self.active

    def get_lasers(self):
        return self.laserlist

if __name__ == "__main__":
    from pygame import *
    from Battlecruiser import *
    from sys import exit


    pygame.init()

    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    screenT = [screen, screen_size[0], screen_size[1]]

    black = (0, 0, 0)

    cruiser = Battlecruiser(screenT,[400, 400])

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


        # Get a font and use it render the text to a Surface.
        font = pygame.font.Font(None, 16)
        screen.fill(black)
        cruiser.draw()
        cruiser.update()

        pygame.display.flip()

import pygame as pg
from pygame.sprite import Sprite
# built in libraries
#import tkinter as tk
from settings import *
import random
from sprites import *
platforms = []

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/14, HEIGHT/3)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 100
    def controls(self):
        keys = pg.key.get_pressed()
        #if keys[pg.K_w]:
             #self.acc.y = -5
        if keys[pg.K_a]:
            self.acc.x = -5
        #if keys[pg.K_s]:
            #dself.acc.y = 5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
             self.jump()
    def jump(self):
        #print("jump has been called...")
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, platforms, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -20
        self.vel.y = -20
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
             print("Game Over")
        # friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos
#platform class
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#healthbar class
class Healthbar(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy:
    def __init__(self, x, y, w, h, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 2
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(BLACK)
        self.screen = screen  # Store the screen object in a class attribute
        self.draw()  # Call the draw method

    def update(self):
        # Update the position of the enemy based on its speed
        self.x += self.speed
        self.y += self.speed
        
        # If the enemy reaches the edge of the screen, reverse its direction
        if self.x < 0 or self.x > WIDTH:
            self.speed = -self.speed
        if self.y < 0 or self.y > HEIGHT:
            self.speed = -self.speed

    def draw(self):
        # Draw the enemy to the screen
        pg.draw.rect(self.screen, self.image, (self.x, self.y, self.w, self.h))


all_platforms = pg.sprite.Group()
'''
my final project is...
'''

'''
sources: 
i used ____ to learn about ____
'''

# import libraries 
import pygame as pg
from pygame.sprite import Sprite

# built in libraries
#import tkinter as tk
from settings import *
import random
#from random import randint

# created libraries
#import settings
#import sprites


# content from kids can code: http://kidscancode.org/blog/

# Mr.Cozort's code

#import the libraries

vec = pg.math.Vector2
WIDTH = 1400
HEIGHT = 720
FPS = 30
# player settings
PLAYER_GRAV = 2   
PLAYER_FRIC = 4
SCORE = 0
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OTHER = (35, 45, 200)
YELLOW = (233, 235, 54)
#defines what the text will look like
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

        


#platforms.
platforms = []
# sprites...
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
        self.health = 1
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

# Define the Enemy class
class Enemy:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pg.Surface((50, 50))
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

# Create an empty array to store the enemies
enemies = []

# Create a new enemy at position (100, 100)
enemy = Enemy(100, 100)

# Add the enemy to the array of enemies

#puts the all_sprites and all_platforms in the pygame sprite group
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# instantiate the player class
player = Player()
#creates the platforms
plat = Platform(400, 400, 50, 1400)
plat2 = Platform(400, 0, 50, 250)
plat3 = Platform(700, 600, 50, 200)
plat4 = Platform(700, 0, 50, 400)
plat5 = Platform(900, 400, 50, 800 )
plat6 = Platform(900, 0, 50, 250)
plat7 = Platform(200, 200, 50, 600)
plat8 = Platform(200, 0, 50, 10)
plat9 = Platform(0, 720, 1400, 10)
plat10 = Platform(1100, 0, 50, 400)
plat11 = Platform(1100, 600, 50, 900)
platr = Platform(0, 0, 10, 720)
platrr = Platform(1390, 10, 10, 720)
platrrr = Platform(0, 0, 1400, 10)
other = Platform(1300, 400, 50, 100)
#adds player to all_sprites
all_sprites.add(player)
#adds platforms to all_sprites
all_sprites.add(plat)
all_sprites.add(plat2)
all_sprites.add(plat3)
all_sprites.add(plat4)
all_sprites.add(plat5)
all_sprites.add(plat6)
all_sprites.add(plat7)
all_sprites.add(plat8)
all_sprites.add(plat9)
all_sprites.add(plat10)
all_sprites.add(plat11)
all_sprites.add(platr)
all_sprites.add(platrr)
all_sprites.add(platrrr)
all_sprites.add(other)
 #adds plats to all_platforms
all_platforms.add(plat)
all_platforms.add(plat2)
all_platforms.add(plat3)
all_platforms.add(plat4)
all_platforms.add(plat5)
all_platforms.add(plat6)
all_platforms.add(plat7)
all_platforms.add(plat8)
all_platforms.add(plat9)
all_platforms.add(plat10)
all_platforms.add(plat11)
all_platforms.add(platr)
all_platforms.add(platrr)
all_platforms.add(platrrr)
all_platforms.add(other)
#adds pltforms to sprites and platform group
all_sprites.add(platforms)
all_platforms.add(platforms)
#loop
running = True
while running:
    #keep the loop running using clock
    clock.tick(FPS)
    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
    
    # updates the sprites
    all_sprites.update()
    all_platforms.update()
    #updates the platforms
       
#if the players velocity is greater than 0 than...
    if player.vel.y > 0:
        #if the player hits the platforms they will stay on the screen
        hits = pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
#platform 1-9, if hit, will move the player to the top of the platform
            (plat, plat9)
            player.pos.y = hits[0].rect.top
            
    elif player.vel.y < 0:
        hits = pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
            all_platforms
            player.rect.top = hits[0].rect.bottom
            
#if the player hits the platforms they stay(False)
    if  hits: 
        pg.sprite.spritecollide(player, all_platforms, False)
#subtracts 1 everytime player hits a platform
        if hits:
            all_platforms
        player.health -= 1    
    elif  hits:
        pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
            all_platforms
            player.health -= 1
    ############ Draw ################
#changes the color of the screen when the players health is less than 0 and is also the backround
    if player.health < 0:
        screen.fill(RED)
    elif player.health > 0:
        screen.fill(BLUE)
#if the players health is below 0 a message will show up on the screen saying the game is over
    if player.health > 0:
        draw_text("HEALTH: " + str(player.health), 22, RED, WIDTH / 2.5, HEIGHT / 
20)
    elif player.health < 0:
        draw_text("YOU LOST!! " + str(player.health), 300, OTHER, WIDTH / 1.5, 
HEIGHT / 20)
    # draw all sprites
    all_sprites.draw(screen)
    
    # buffer - after drawing everything, flip display
    pg.display.flip()
pg.quit()
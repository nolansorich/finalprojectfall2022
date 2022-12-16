# Nolan Sorich


'''
sources: 
content from kids can code: http://kidscancode.org/blog/
Youtube
Mr.Cozort's code
'''


# import libraries 
import pygame as pg
from pygame.sprite import Sprite
# built in libraries
#import tkinter as tk
from settings import *
import random
from sprites import *
#from random import randint

# created libraries
#import settings
#import sprites

#import the libraries


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

# Create a sprite group
all_sprites = pg.sprite.Group()

# Create an instance of the Enemy class
# Create a sprite group
all_sprites = pg.sprite.Group()

# Create an instance of the Enemy class
enemy = Enemy(50, 50, 1250, 200)
enemies = pg.sprite.Group()
enemies.add(enemy)
# Add the enemy to the sprite group
all_sprites.add(enemy)

# Draw the sprite group on the surface
all_sprites.draw(screen)

all_platforms = pg.sprite.Group()
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
platrrr = Platform(0, -70, 1400, 10)

#adds player to all_sprites
all_sprites.add(player)

all_sprites.add(enemy)

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
#all_sprites.add(other)
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
#all_platforms.add(other)
#adds pltforms to sprites and platform group
all_sprites.add(platforms)
all_platforms.add(platforms)
#loop
running = True
while running:
    # Keep the loop running using clock
    clock.tick(FPS)
    for event in pg.event.get():
        # Check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
    
    # Create separate variables for checking collisions between the player and platforms, and between the player and enemies
    hits_platforms = pg.sprite.spritecollide(player, all_platforms, False)
    hits_enemies = pg.sprite.spritecollide(player, enemies, False)
    
    # Check for collisions between the player and platforms
    if hits_platforms:
        # Move the player to the top of the platform
        player.pos.y = hits_platforms[0].rect.top
        player.health -= 1
    
    # Check for collisions between the player and enemies
    if hits_enemies:
        # Decrease the health of both the player and the enemy
        player.health += 1
        enemy.health -= 1
        
    # Check if the player is colliding with the enemy
    if player.rect.colliderect(enemy.rect):
        # Hit the enemy
        enemy.hit()
    
    # Check if the enemy is dead or has been hit
    if enemy.health <= 0 or enemy.is_hit:
        # Remove the enemy from the game
        enemy.kill()
    
    # Update the sprites and platforms
    all_sprites.update()
    all_platforms.update()
    
        

    ############ Draw ################
# changes backround to White when enemy health
    if enemy.health < 0:
        screen.fill(WHITE)
        draw_text("WINNER!! " + str(player.health), 300, OTHER, WIDTH / 1.5, HEIGHT / 20)

# If the enemy's health is greater than or equal to 0, the screen will be filled with blue
    else:
        screen.fill(BLUE)

# Check the player's health and fill the screen with red if it is less than 0
    if player.health < 0:
        screen.fill(RED)
        draw_text("YOU LOST!! " + str(player.health), 300, OTHER, WIDTH / 1.5, HEIGHT / 20)

# If the player's health is greater than or equal to 0, display their health
    else:
        draw_text("HEALTH: " + str(player.health), 22, RED, WIDTH / 2.5, HEIGHT / 20)

# Draw all sprites
    all_sprites.draw(screen)

# Buffer - after drawing everything, flip display
    pg.display.flip()


pg.quit()
#SpaceInvaders.py geeksforgeeks  
# 0 STEAL EVERYTHING FROM THE INTERNET, YOUTUBE, AND FREESOUND! *RECOMMENDED FOR NOOBS*
# 1 remove.bg - remove background from image
# 2a imageresizer.com - resize image
# 2b upscale.media is an AI image resizer that can upscale your image to 2x or 4x without losing any textures or details.
# 3a FL Studio - Music Maker
# 3b Beepbox + every mod - Music Maker
# 3c Chrome Music Lab - Music Maker
# 3d OpenMPT - Music Maker
# 3e FamiTracker - Music Maker
# 4a Leonardo.ai - AI Art Generator
# 4b Scratch - Paint Editor, Sound Editor
# 4c Figma - Paint Editor

### BE CAREFUL! YOU ONLY HAVE TO CHOOSE ONE! ###

import pygame
import random
import math
from pygame import mixer
import time

# Initialize pygame
pygame.init()

# Create screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
# The ratio is 16:9

# Caption and icon
pygame.display.set_caption("Welcome to Space Invaders by Morphing Under Night Armor")

# Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.SysFont("Dosis", 40)

# Game Over
game_over_font = pygame.font.SysFont("Dosis", 128)

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (0,255,0))
    screen.blit(score, (x, y))

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(game_over_text, (400, 500))

# Background Sound
mus = random.randint(1,2)
if mus == 1:
    mixer.music.load("SpaceInvaders/assets/audio/uplift - awesome HIGH QUALITY.wav")
elif mus == 2:
    mixer.music.load("SpaceInvaders/assets/audio/uplift - lols HIGH QUALITY.wav")
mixer.music.play(-1)

# Player
playerImage = pygame.image.load("SpaceInvaders/assets/img/KingsnakePlane.png")
player_X = 740
player_Y = 785
player_Xchange = 0
player_Ychange = 0

# Invader
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 20

for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load('SpaceInvaders/assets/img/Albatros D.V.png'))
    invader_X.append(random.randint(128, 1472))
    invader_Y.append(random.randint(60, 400))
    invader_Xchange.append(1.2)
    invader_Ychange.append(75)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = pygame.image.load("SpaceInvaders/assets/img/bullet.png")
bullet_X = 0
bullet_Y = 500
bullet_X2 = 0
bullet_Y2 = 500
bullet_X3 = 0
bullet_Y3 = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"
bullet_state2 = "rest"
bullet_state3 = "rest"

# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y1 - y2,2)))
    if distance <= 100:
        return True
    else:
        return False

def player(x, y):
    screen.blit(playerImage, (x - 50, y - 50))

def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"
def bullet2(x, y):
    global bullet_state2
    screen.blit(bulletImage, (x, y))
    bullet_state2 = "fire"
def bullet3(x, y):
    global bullet_state3
    screen.blit(bulletImage, (x, y))
    bullet_state3 = "fire"

isitagameover = 0
bullets_left = 3

# game loop
running = True
frames = 0
ScorePointBGchange = 0
while running:
    frames += 1
    # RGB
    screen.fill((abs(math.sin(ScorePointBGchange*32)*(ScorePointBGchange%255)), 0, 0))
    ScorePointBGchange += (0 - ScorePointBGchange)/5
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            running = False
        # Control player movement from arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -2
            if event.key == pygame.K_RIGHT:
                player_Xchange = 2
            if event.key == pygame.K_UP:
                player_Ychange = -2
            if event.key == pygame.K_DOWN:
                player_Ychange = 2
            if event.key == pygame.K_SPACE:
                # Fix change of direction of bullet
                if bullet_state == "rest" and bullets_left == 3:
                    bullet_X = player_X
                    bullet_Y = player_Y
                    bullet(bullet_X, bullet_Y)
                    bullet_sound = mixer.Sound('SpaceInvaders/assets/audio/gunshot1.wav')
                    bullet_sound.play()
                    bullets_left -= 1
                elif bullet_state2 == "rest" and bullets_left == 2:
                    bullet_X2 = player_X
                    bullet_Y2 = player_Y
                    bullet2(bullet_X2, bullet_Y2)
                    bullet_sound = mixer.Sound('SpaceInvaders/assets/audio/gunshot1.wav')
                    bullet_sound.play()
                    bullets_left -= 1
                elif bullet_state3 == "rest" and bullets_left == 1:
                    bullet_X3 = player_X
                    bullet_Y3 = player_Y
                    bullet3(bullet_X3, bullet_Y3)
                    bullet_sound = mixer.Sound('SpaceInvaders/assets/audio/gunshot1.wav')
                    bullet_sound.play()
                    bullets_left -= 1
        if event.type == pygame.KEYUP:
            player_Xchange = 0
            player_Ychange = 0
    # Add the change in the player position
    player_X += player_Xchange
    player_Y += player_Ychange
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]
        
    # Bullet movement
    if bullet_Y <= 0:
        bullet_Y = 900
        bullet_state = "rest"
        bullets_left += 1
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange
    if bullet_Y2 <= 0:
        bullet_Y2 = 900
        bullet_state2 = "rest"
        bullets_left += 1
    if bullet_state2 == "fire":
        bullet2(bullet_X2, bullet_Y2)
        bullet_Y2 -= bullet_Ychange
    if bullet_Y3 <= 0:
        bullet_Y3 = 900
        bullet_state3 = "rest"
        bullets_left += 1
    if bullet_state3 == "fire":
        bullet3(bullet_X3, bullet_Y3)
        bullet_Y3 -= bullet_Ychange
    

    # Movement of the invader
    for i in range(no_of_invaders):
        if invader_Y[i] >= 650:
            if abs(player_X-invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                if (isitagameover == 0):
                    explosion_sound = mixer.Sound('SpaceInvaders/assets/audio/explosion.wav')
                    explosion_sound.play()
                    mixer.music.stop()
                    game_over()
                    isitagameover = 1
                    ScorePointBGchange = 500
                    break
        if invader_X[i] >= 1473 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]
        # Collision
        collision = isCollision(bullet_X, invader_X[i], bullet_Y, invader_Y[i])
        collision2 = isCollision(bullet_X2, invader_X[i], bullet_Y2, invader_Y[i])
        collision3 = isCollision(bullet_X3, invader_X[i], bullet_Y3, invader_Y[i])
        if collision or collision2 or collision3:
            score_val += 1
            ScorePointBGchange += 360
            explosion2_sound = mixer.Sound('SpaceInvaders/assets/audio/explosion1.wav')
            explosion2_sound.play()
            if collision:
                bullet_Y = 900
                bullet_state = "rest"
            elif collision2:
                bullet_Y2 = 900
                bullet_state2 = "rest"
            elif collision3:
                bullet_Y3 = 900
                bullet_state3 = "rest"
            bullets_left += 1
            invader_X[i] = random.randint(128, 1472)
            invader_Y[i] = random.randint(60, 400)
            invader_Xchange[i] *= -1
        invader(invader_X[i], invader_Y[i], i)

    # Restrict the spaceship so that it doesn't go offscreen
    if player_X <= 50:
        player_X = 50
    elif player_X >= 1500:
        player_X = 1500
    if player_Y <= 50:
        player_Y = 50
    elif player_Y >= 800:
        player_Y = 800
    
    if isitagameover == 1:
        game_over()
    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    pygame.display.update()

while running:
    frames += 1
    # RGB
    screen.fill((abs(math.sin(ScorePointBGchange*32)*(ScorePointBGchange%255)), 0, 0))
    ScorePointBGchange += (0 - ScorePointBGchange)/5
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            running = False

# https://www.popularmechanics.com/military/aviation/a35865601/f-36-kingsnake-air-force-next-fighter-jet-concept/
# https://www.transparentpng.com/details/bullet-hd-photo-_22792.html
# https://www.pngwing.com/en/free-png-papmh
# Deltarune - Bad Explosion
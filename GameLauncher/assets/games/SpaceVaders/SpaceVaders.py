# July 8 - August 19, 2024

import decimal
from decimal import *
import pygame
from pygame import *
import time
import math
import sys
import os
import random
import keyboard
# https://youtu.be/FfWpgLFMI7w?t=4331
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_collision_and_intesection.md
# https://icons8.com/icons/set/space-invaders--animated
# https://www.freepik.com/free-vector/futuristic-spaceship-collection-with-flat-design_2898820.htm#query=space%20fighter&position=1&from_view=keyword&track=ais_user&uuid=5e43d284-9e98-4b88-a912-680fec6643a0
# https://www.freepik.com/free-vector/funny-game-monsters-collection_1529196.htm#fromView=search&page=2&position=7&uuid=20b22d67-42fc-4208-b742-6e63656f1697
# https://www.youtube.com/watch?v=F69-t33e8tk
# https://www.freepik.com/free-vector/hand-painted-watercolor-galaxy-background_14237502.htm#fromView=search&page=1&position=0&uuid=801401a5-0317-4fcc-a9aa-ff0df8e0039f

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

playlist = list()
playlist.append ( "./GameLauncher/assets/games/SpaceVaders/audio/Kevin MacLeod - Space Fighter Loop.mp3" )
playlist.append ( "./GameLauncher/assets/games/SpaceVaders/audio/Kevin MacLeod - Mesmerizing Galaxy Loop.mp3" )
playlist.append ( "./GameLauncher/assets/games/SpaceVaders/audio/Kevin MacLeod - Galactic Rap.mp3" )
playlist.append ( "./GameLauncher/assets/games/SpaceVaders/audio/Kevin MacLeod - Cloud Dancer.mp3" )
playlist.append ( "./GameLauncher/assets/games/SpaceVaders/audio/Kevin MacLeod - Brain Dance.mp3" )

pygame.mixer.music.load ( playlist.pop() )  
pygame.mixer.music.queue ( playlist.pop() )
pygame.mixer.music.set_endevent ( pygame.USEREVENT )  
pygame.mixer.music.play(-1)

# Title and Icon and background
pygame.display.set_caption("Space Vaders")
icon = pygame.image.load('./GameLauncher/assets/games/SpaceVaders/img/SPACE FIGHTERS SVG icons8.png')
pygame.display.set_icon(icon)
background = pygame.image.load('./GameLauncher/assets/games/SpaceVaders/img/5438849.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))
backgroundRect = pygame.Rect(background.get_rect())
backgroundRect.clamp_ip(pygame.display.get_surface().get_rect())

# Player
playerImg = pygame.image.load('./GameLauncher/assets/games/SpaceVaders/img/player.png')
playerPos = [(1280 - playerImg.get_width()/2.5)/2, (720 - playerImg.get_height()/2.5)/2 + 240]
playerPosChange = [0, 0]
playerRect = pygame.Rect(playerImg.get_rect())

def player():
    playerImg = pygame.image.load('./GameLauncher/assets/games/SpaceVaders/img/player.png')
    playerImg = pygame.transform.scale(playerImg, (playerImg.get_width()/2.5 * WindowScale, playerImg.get_height()/2.5 * WindowScale))
    playerRect = pygame.Rect(playerImg.get_rect())
    playerRect.clamp_ip(pygame.display.get_surface().get_rect())
    screen.blit(playerImg, (playerPos[0]*WindowXscale, playerPos[1]*WindowYscale))

# Enemy
enemyImageNumber = random.randint(1,9)
enemyImg = pygame.image.load(f"./GameLauncher/assets/games/SpaceVaders/img/alien{enemyImageNumber}.png")
enemyPos = [random.randint(0, screen_width), random.randint(50, 200)]
enemyPosChange = [60, 0]
enemyRect = pygame.Rect(enemyImg.get_rect())

def enemy():
    enemyImg = pygame.image.load(f"./GameLauncher/assets/games/SpaceVaders/img/alien{enemyImageNumber}.png")
    enemyImg = pygame.transform.scale(enemyImg, (enemyImg.get_width()*WindowScale/15, enemyImg.get_height()*WindowScale/15))
    enemyRect = pygame.Rect(enemyImg.get_rect())
    enemyRect.clamp_ip(pygame.display.get_surface().get_rect())
    screen.blit(enemyImg, (enemyPos[0]*WindowXscale, enemyPos[1]*WindowYscale))

# Game Loop
running = True
frames = 0
start_time = time.time()
delta_time = 0.000001
game_time = -0.000001
GameFPS = 1/delta_time #60
def constrain(val, min_val, max_val):
    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

particles = []

while running:
    mos_x, mos_y = pygame.mouse.get_pos()
    frames += 1
    (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
    WindowXscale = WindowWidth / screen_width
    WindowYscale = WindowHeight / screen_height
    if WindowXscale < 0.01 and WindowYscale < 0.01:
        WindowScale = min(WindowXscale, WindowYscale)
    elif WindowXscale > 0.01 and WindowYscale > 0.01:
        WindowScale = min(WindowXscale, WindowYscale)
    else:
        WindowScale = 0.01
    delta_time = (time.time() - start_time) - game_time
    game_time = time.time() - start_time
    if delta_time > 0:
        GameFPS = 1/delta_time
    else:
        GameFPS = math.inf
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether its right or left
    if keyboard.is_pressed('up'):
        playerPosChange[1] -= 12 * delta_time
    if keyboard.is_pressed('down'):
        playerPosChange[1] += 12 * delta_time
    if keyboard.is_pressed('left'):
        playerPosChange[0] -= 12 * delta_time
    if keyboard.is_pressed('right'):
        playerPosChange[0] += 12 * delta_time

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 32))
    # Background Image
    background = pygame.image.load('./GameLauncher/assets/games/SpaceVaders/img/5438849.jpg')
    background = pygame.transform.scale(background, (WindowWidth, WindowHeight))
    screen.blit(background, (0, 0))
    particles.append([[random.randint(screen_width*-1, screen_width), -100], [random.randint(0, 0) / 10 - 1, 300], random.randint(4, 6), -2])

    for particle in particles:
        particle[0][0] += particle[1][0] * delta_time
        particle[0][1] += particle[1][1] * delta_time
        particle[2] += particle[3] * delta_time
        pygame.draw.circle(screen, (255, 255, 255), (particle[0][0]*WindowXscale, particle[0][1]*WindowYscale), particle[2]*WindowScale)
        if particle[2] <= 0:
            particles.remove(particle)

    playerPos[0] += playerPosChange[0] * 100 * delta_time
    playerPos[1] += playerPosChange[1] * 100 * delta_time
    playerPosChange[0] *= 0.04**delta_time
    playerPosChange[1] *= 0.04**delta_time
    #playerPos[0] = constrain(playerPos[0], 0, screen_width - 135*WindowScale)
    #playerPos[1] = constrain(playerPos[1], 0, screen_height - 165*WindowScale)
    enemyPos[0] += enemyPosChange[0] * delta_time
    enemyPos[1] += enemyPosChange[1] * delta_time
    if WindowXscale >= WindowYscale:
        playerPos[0] = constrain(playerPos[0], 0, screen_width - playerImg.get_width()*WindowScale/2.5)
        if enemyPos[0] >= screen_width - enemyImg.get_width()*WindowScale/15 or enemyPos[0] <= 0:
            enemyPos[0] -= enemyPosChange[0]/10
            enemyPosChange[0] *= -1.2
            enemyPos[1] += 40
    else:
        playerPos[0] = constrain(playerPos[0], 0, screen_width - playerImg.get_width()/2.5)
        if enemyPos[0] >= screen_width - enemyImg.get_width()/15 or enemyPos[0] <= 0:
            enemyPos[0] -= enemyPosChange[0]/10
            enemyPosChange[0] *= -1.2
            enemyPos[1] += 40
    if WindowYscale >= WindowXscale:
        playerPos[1] = constrain(playerPos[1], 0, screen_height - playerImg.get_height()*WindowScale/2.5)
    else:
        playerPos[1] = constrain(playerPos[1], 0, screen_height - playerImg.get_height()/2.5)
    player()
    enemy()
    pygame.display.flip()
    pygame.display.update()
    #clock.tick(24)
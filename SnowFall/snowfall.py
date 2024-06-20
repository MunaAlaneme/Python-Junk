import pygame
import time
import random
import pyautogui
from pygame import *
import math
pygame.init()

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
RED = [255, 0, 0]
WIDTH, HEIGHT = pyautogui.size()
SIZE = [int(WIDTH), int(HEIGHT*0.9)]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("MunaAlaneme - Snow Fall")

snowFall = []
for i in range(300):
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    snowFall.append([x, y])
clock = pygame.time.Clock()
done = False
frames = 0
while not done:
    frames += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
    screen.fill((0, 0, 0))
    for i in range(len(snowFall)):
        pygame.draw.circle(screen, (128+(math.sin((frames+i)*12.5)*128), 128+(math.cos((frames+i)*25)*128), 128+(math.sin(math.cos((frames+i)*20)*128))), snowFall[i], 2)
        snowFall[i][1] += 1
        if snowFall[i][1] > int(HEIGHT*0.9):
            y = random.randrange(-50, -10)
            snowFall[i][1] = y
            x = random.randrange(0, 400)
            snowFall[1][0] = x
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
# https://www.geeksforgeeks.org/snowfall-display-using-pygame-in-python/
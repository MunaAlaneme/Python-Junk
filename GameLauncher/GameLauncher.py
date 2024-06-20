import random
import tkinter
from tkinter import *
from tkinter import ttk
import pygame as pygaming
import math
import sys
from decimal import *
import time
import PyQt5
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

print("\u2226")
print("\u1300")
print("\u3522")
print("\u5483")
print("\u2375")
print("\u0352")
print("\u5698")

print("\U0001F234")
print("\U0001F567")
print("\U0001F890")
print("\U0001F123")
print("\U0001F456")
print("\U0001F789")
print("\U0001F012")

if 7 != 7:
    print("Correct")
else:
    print("I don't understand you. Did you mean 7 == 7?")

# Initialize Pygame
pygaming.init()

# Constants
SCREEN_WIDTH = 820
SCREEN_HEIGHT = 300

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
(TargetButtonColorRed, TargetButtonColorGreen, TargetButtonColorBlue) = ([200, 200, 200, 200, 200, 200, 200, 200, 200], [200, 200, 200, 200, 200, 200, 200, 200, 200], [200, 200, 200, 200, 200, 200, 200, 200, 200]) #(200, 200, 200)
(ButtonColorRed, ButtonColorGreen, ButtonColorBlue) = ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]) #(0, 0, 0)
GameNames = ("1. Snake", "2. Flappy Bird", "3. GUI Calculator", "4. Slide Puzzle", "5. Space Invaders", "6. SnowFall", "7. Auto Tic Tac Toe", "8. Manual Tic Tac Toe", "9. Clicker Game")

# Create the screen
screen = pygaming.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),  pygaming.RESIZABLE)
pygaming.display.set_caption('Game Launcher')
def PlayMusic(musNum):
    if musNum == 1:
        pygaming.mixer.music.load("GameLauncher/assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav")
    elif musNum == 2:
        pygaming.mixer.music.load("GameLauncher/assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav")
    pygaming.mixer.music.play(-1)
PlayMusic(random.randint(1,2))

# Create a font for the button text
font = pygaming.font.Font(None, 36)

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

# Create a list to store buttons
buttons = []

# Create buttons and add them to the list

# Game loop
running = True
hovering_a_button2 = 0
y_scroll = 0
y_scroll_vel = 0
start_time = time.time()
delta_time = 0.0001
game_time = -0.0001
while running:
    delta_time = (time.time() - start_time) - game_time
    game_time = time.time() - start_time
    mos_x, mos_y = pygaming.mouse.get_pos()
    buttons = []
    (WindowWidth, WindowHeight) = pygaming.display.get_surface().get_size()
    if mos_y > WindowHeight/1.2:
        y_scroll_vel -= 20*delta_time
    elif mos_y < WindowHeight/10:
        y_scroll_vel += 20*delta_time
    y_scroll = constrain(y_scroll+y_scroll_vel, SCREEN_HEIGHT/-1.2, SCREEN_HEIGHT/1.2)
    y_scroll_vel /= 1.1
    xscale = WindowWidth / SCREEN_WIDTH
    yscale = WindowHeight / SCREEN_HEIGHT
    if xscale < 1 and yscale < 1:
        scale = max(xscale, yscale)
    elif xscale > 1 and yscale > 1:
        scale = min(xscale, yscale)
    else:
        scale = 1.0
    if xscale < .1 and yscale < .1:
        scale2 = min(xscale, yscale)
    elif xscale > .1 and yscale > .1:
        scale2 = min(xscale, yscale)
    else:
        scale2 = 0.1
    font = pygaming.font.Font("./fonts/Dosis/static/Dosis-Bold.ttf", int(28*scale2))
    BUTTON_WIDTH = (120, 180, 220, 200, 220, 160, 260, 260, 220)
    (BUTTON_X_POS, BUTTON_Y_POS) = ([20, 160, 360, 600, 20, 260, 440, 20, 300], ((SCREEN_HEIGHT // 2) - 125, (SCREEN_HEIGHT // 2) - 125, (SCREEN_HEIGHT // 2) - 125, (SCREEN_HEIGHT // 2) - 125, (SCREEN_HEIGHT // 2) - 25, (SCREEN_HEIGHT // 2) - 25, (SCREEN_HEIGHT // 2) - 25, (SCREEN_HEIGHT // 2) + 75, (SCREEN_HEIGHT // 2) + 75))

    BUTTON_HEIGHT = 50
    BUTTON_GAP_Y = 20
    for i in range(9):
        button_rect = pygaming.Rect(
            BUTTON_X_POS[i]*xscale,
            (BUTTON_Y_POS[i] + y_scroll)*yscale,
            BUTTON_WIDTH[i]*xscale,
            BUTTON_HEIGHT*yscale
        )
        buttons.append(button_rect)

    # Draw background
    screen.fill((255, 0, 200))

    hovering_a_button = 0

    # Draw buttons and text
    for i, button in enumerate(buttons):
        ButtonColorRed[i] += (TargetButtonColorRed[i] - ButtonColorRed[i])/10
        ButtonColorGreen[i] += (TargetButtonColorGreen[i] - ButtonColorGreen[i])/10
        ButtonColorBlue[i] += (TargetButtonColorBlue[i] - ButtonColorBlue[i])/10
        pygaming.draw.rect(screen, (ButtonColorRed[i], ButtonColorGreen[i], ButtonColorBlue[i]), button)
        pygaming.draw.rect(screen, BLACK, button, int(4*scale))

        # Highlight the button when the mouse is over it
        if button.collidepoint(pygaming.mouse.get_pos()):
            pygaming.draw.rect(screen, GREEN, button, int(2*scale))
            TargetButtonColorRed[i] = 0
            TargetButtonColorGreen[i] = 255
            TargetButtonColorBlue[i] = 0
            hovering_a_button = i+1
        else:
            TargetButtonColorRed[i] = 200
            TargetButtonColorGreen[i] = 200
            TargetButtonColorBlue[i] = 200

        # Render and draw centered text on the button
        text = font.render(GameNames[i], True, BLACK)
        text_rect = text.get_rect(center=button.center)
        screen.blit(text, text_rect)
    if hovering_a_button2 != hovering_a_button:
        HoverSound = pygaming.mixer.Sound("GameLauncher/assets/audio/251389__deadsillyrabbit__button_hover-wav.wav")
        if hovering_a_button != 0:
            HoverSound.play()
        hovering_a_button2 = hovering_a_button

    # Update the display
    pygaming.display.flip()
    pygaming.display.update()

    for event in pygaming.event.get():
        if event.type == pygaming.QUIT:
            pygaming.quit()
            running = False
            sys.exit()

        # Check for mouse button click
        if event.type == pygaming.MOUSEBUTTONDOWN and event.button == 1:
            # Check if any button is clicked
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    if 7 == 7:
                        pygaming.mixer.music.stop()
                        pygaming.quit()
                        running = False
                        if (i+1) == 1:
                            from assets.games.SnakeGame import SnakeGame
                        elif (i+1) == 2:
                            from assets.games.FlappyBird import FlappyBird
                        elif (i+1) == 3:
                            from assets.apps.GUICalculator import GUICalculator
                        elif (i+1) == 4:
                            from assets.games.SlidePuzzle import SlidePuzzle
                        elif (i+1) == 5:
                            from assets.games.SpaceInvaders import SpaceInvaders
                        elif (i+1) == 6:
                            import assets.apps.SnowFall.snowfall as snowfall
                        elif (i+1) == 7:
                            from assets.games.TicTacToe import AutoTicTacToe
                        elif (i+1) == 8:
                            from assets.games.TicTacToe import ManualTicTacToe
                        elif (i+1) == 9:
                            from assets.games.ClickerGame import ClickerGame
                        screen = pygaming.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),  pygaming.RESIZABLE)
                        pygaming.display.set_caption('Game Launcher')
                        running = True
                        pygaming.init()
                        PlayMusic(random.randint(1,2))
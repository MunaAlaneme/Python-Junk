# Credits!!!
# Google Bard - Help
# OpenAI ChatGPT - Help
# Microsoft Bing AI Chat Copilot - Help
# (YT) Clear Code - Particle System
# jay3332 - Number Abbreviation

import pygame
import random
from decimal import *
import math
import sys
import time
import os
import numpy as np

GameFPS = 60

class ParticlePrinciple:
    def __init__(self):
        self.particles = []
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
                WindowXscale = WindowWidth / screen_width
                WindowYscale = WindowHeight / screen_height
                if WindowXscale < 0 and WindowYscale < 0:
                    WindowScale2 = min(WindowXscale, WindowYscale)
                elif WindowXscale > 0 and WindowYscale > 0:
                    WindowScale2 = min(WindowXscale, WindowYscale)
                else:
                    WindowScale2 = 0
                particle[0][0] += particle[3] * math.sin(particle[2]) * 60/GameFPS * WindowScale2
                particle[0][1] += particle[3] * math.cos(particle[2]) * 60/GameFPS * WindowScale2
                particle[1] -= 24/GameFPS
                pygame.draw.circle(screen, pygame.Color('White'), particle[0], particle[1]*WindowScale2)
    def add_particles(self, posx, posy, radiuss, directionn, sped):
        pos_x = posx
        pos_y = posy
        radius = radiuss
        direction = directionn
        speed = sped
        particle_circle = [[pos_x, pos_y], radius, direction, speed]
        self.particles.append(particle_circle)
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

# Initialize Pygame
pygame.init()

# Long Suffixes Add
for _ in range(1):
    LongSuffixes = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion"]
    UniSuffixes = ["", "un", "duo", "tre", "quattor", "quin", "sex", "septen", "octo", "novem", ""]
    BiSuffixes = ["", "decillion", "vigintillion", "trigintillion", "quadragintillion", "quinquagintillion", "sexagintillion", "septuagintillion", "octogintillion", "nonagintillion", ""]
    BiSuffixesShort = ["", "deci", "viginti", "triginti", "quadraginti", "quinquaginti", "sexaginti", "septuaginti", "octoginti", "nonaginti", ""]
    TriSuffixes = ["", "centillion", "ducentillion", "trecentillion", "quadracentillion", "quintacentillion", "sesagintillion", "septacentillion", "octocentillion", "nongincentillion", ""]
    TriSuffixesShort = ["", "centi", "ducenti", "trecenti", "quadracenti", "quintacenti", "sesaginti", "septacenti", "octogincenti", "nongincenti", ""]
    QuadSuffixes = ["", "millillion", "dumillillion", "trimillillion", "quadrimillillion", "quinmillillion", "sexamillillion", "septimillillion", "octomillillion", "nonamillillion", ""]
    unicount = 1
    bicount = 1
    for _ in range(9):
        for _ in range(9):
            LongSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount])
            unicount += 1
        LongSuffixes.append(BiSuffixes[bicount+1])
        unicount = 1
        bicount += 1
    tricount = 1
    for _ in range(9):
        LongSuffixes[len(LongSuffixes)-1] = TriSuffixes[tricount]
        unicount = 1
        for _ in range(9):
            LongSuffixes.append(UniSuffixes[unicount] + TriSuffixes[tricount])
            unicount += 1
        unicount = 1
        bicount = 1
        LongSuffixes.append(BiSuffixesShort[bicount] + TriSuffixes[tricount])
        for _ in range(9):
            for _ in range(9):
                LongSuffixes.append(UniSuffixes[unicount] + BiSuffixesShort[bicount] + TriSuffixes[tricount])
                unicount += 1
            LongSuffixes.append(BiSuffixesShort[bicount+1] + TriSuffixes[tricount])
            unicount = 1
            bicount += 1
        tricount += 1
    LongSuffixes[len(LongSuffixes)-1] = "millillion"
    quadcount = 1
    for _ in range(9):
        LongSuffixes[len(LongSuffixes)-1] = QuadSuffixes[quadcount]
        unicount = 1
        for _ in range(9):
            LongSuffixes.append(UniSuffixes[unicount] + QuadSuffixes[quadcount])
            unicount += 1
        unicount = 1
        bicount = 1
        LongSuffixes.append(BiSuffixesShort[bicount] + QuadSuffixes[quadcount])
        for _ in range(9):
            for _ in range(9):
                LongSuffixes.append(UniSuffixes[unicount] + BiSuffixesShort[bicount] + QuadSuffixes[quadcount])
                unicount += 1
            LongSuffixes.append(BiSuffixesShort[bicount+1] + QuadSuffixes[quadcount])
            unicount = 1
            bicount = 1
        tricount = 1
        for _ in range(9):
            LongSuffixes[len(LongSuffixes)-1] = TriSuffixesShort[tricount] + QuadSuffixes[quadcount]
            unicount = 1
            for _ in range(9):
                LongSuffixes.append(UniSuffixes[unicount] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
                unicount += 1
            unicount = 1
            bicount = 1
            LongSuffixes.append(BiSuffixesShort[bicount] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
            for _ in range(9):
                for _ in range(9):
                    LongSuffixes.append(UniSuffixes[unicount] + BiSuffixesShort[bicount] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
                    unicount += 1
                LongSuffixes.append(BiSuffixesShort[bicount+1] + TriSuffixesShort[tricount] + QuadSuffixes[quadcount])
                unicount = 1
                bicount += 1
            tricount += 1
        quadcount += 1
    LongSuffixes[len(LongSuffixes)-1] = "myrnillion"
    LongSuffCount = 1
    for _ in range(len(LongSuffixes)):
        LongSuffixes[LongSuffCount-1] = " " + LongSuffixes[LongSuffCount-1]
        LongSuffCount += 1

# Short Suffixes Add
for _ in range(1):
    ShortSuffixes = ["", "k", "M", "B", "T", "Qa", "Qi", "Sx", "Sp", "O", "N", "d"]
    UniSuffixes = ["", "U", "D", "T", "Qa", "Qi", "Sx", "Sp", "O", "N", ""]
    BiSuffixes = ["", "d", "Vg", "Tg", "Qag", "Qig", "Sxg", "Spg", "Og", "Ng", ""]
    TriSuffixes = ["", "Cnt", "Ducnt", "Trcnt", "Qacnt", "Qicnt", "Secnt", "Spcnt", "Ocnt", "Ncnt", ""]
    QuadSuffixes = ["", "Mlln", "Dmln", "Tmln", "Qdmln", "Qimln", "Sxmln", "Spmln", "Omln", "Nmln", ""]
    unicount = 1
    bicount = 1
    for _ in range(9):
        for _ in range(9):
            ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount])
            unicount += 1
        ShortSuffixes.append(BiSuffixes[bicount+1])
        unicount = 1
        bicount += 1
    tricount = 1
    for _ in range(9):
        ShortSuffixes[len(ShortSuffixes)-1] = TriSuffixes[tricount]
        unicount = 1
        for _ in range(9):
            ShortSuffixes.append(UniSuffixes[unicount] + TriSuffixes[tricount])
            unicount += 1
        unicount = 1
        bicount = 1
        ShortSuffixes.append(BiSuffixes[bicount] + TriSuffixes[tricount])
        for _ in range(9):
            for _ in range(9):
                ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount] + TriSuffixes[tricount])
                unicount += 1
            ShortSuffixes.append(BiSuffixes[bicount+1] + TriSuffixes[tricount])
            unicount = 1
            bicount += 1
        tricount += 1
    ShortSuffixes[len(ShortSuffixes)-1] = "Mlln"
    quadcount = 1
    for _ in range(9):
        ShortSuffixes[len(ShortSuffixes)-1] = QuadSuffixes[quadcount]
        unicount = 1
        for _ in range(9):
            ShortSuffixes.append(UniSuffixes[unicount] + QuadSuffixes[quadcount])
            unicount += 1
        unicount = 1
        bicount = 1
        ShortSuffixes.append(BiSuffixes[bicount] + QuadSuffixes[quadcount])
        for _ in range(9):
            for _ in range(9):
                ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount] + QuadSuffixes[quadcount])
                unicount += 1
            ShortSuffixes.append(BiSuffixes[bicount+1] + QuadSuffixes[quadcount])
            unicount = 1
            bicount = 1
        tricount = 1
        for _ in range(9):
            ShortSuffixes[len(ShortSuffixes)-1] = TriSuffixes[tricount] + QuadSuffixes[quadcount]
            unicount = 1
            for _ in range(9):
                ShortSuffixes.append(UniSuffixes[unicount] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
                unicount += 1
            unicount = 1
            bicount = 1
            ShortSuffixes.append(BiSuffixes[bicount] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
            for _ in range(9):
                for _ in range(9):
                    ShortSuffixes.append(UniSuffixes[unicount] + BiSuffixes[bicount] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
                    unicount += 1
                ShortSuffixes.append(BiSuffixes[bicount+1] + TriSuffixes[tricount] + QuadSuffixes[quadcount])
                unicount = 1
                bicount += 1
            tricount += 1
        quadcount += 1
    ShortSuffixes[len(ShortSuffixes)-1] = "Myrn"

def fexp(f):
    return Decimal(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(f))))) if f != 0 else 0

def fman(f):
    return Decimal(f/10**fexp(f))

def abbreviate(number, suffixes, decimals, greaterthan):
    if number < greaterthan:
        return round(number*(10**decimals))/(10**decimals)
    if fexp(Decimal(number)) < 10002 * 3 and fexp(Decimal(number)) > -1:
        if suffixes == "l":
            return (str(round(fman(Decimal(number)) * (10**(fexp(Decimal(number))%3)) * (10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3)-decimals)))) / 10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals)) + LongSuffixes[Decimal.__floor__(Decimal(fexp(Decimal(number))/3))+0])
        elif suffixes == "s":
            return (str(round(fman(Decimal(number)) * (10**(fexp(Decimal(number))%3)) * (10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals))) / 10**Decimal.__abs__(Decimal((fexp(Decimal(number))%3))-decimals)) + ShortSuffixes[Decimal.__floor__(Decimal(fexp(Decimal(number))/3))+0])
    elif Decimal.__abs__(Decimal(fexp(Decimal(number)))) < 10**6:
        return (str(round(fman(Decimal(number)), decimals)) + "e" + str(fexp(Decimal(number))))
    elif Decimal.__abs__(Decimal(fexp(Decimal(number)))) < 10**10002 * 3:
        if suffixes == "l":
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)*3), 3)) + LongSuffixes[Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)+0])
        elif suffixes == "s":
            return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)*3), 3)) + ShortSuffixes[Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))/3)+0])
    else:
        return (str(round(fman(Decimal(number)), decimals)) + "e" + str(round(fexp(Decimal(number)) / 10**(Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number))))))), 3)) + "e" + Decimal.__floor__(Decimal.log10(Decimal.__abs__(Decimal(fexp(Decimal(number)))))))

# Screen and clock
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Clicker Game")
clock = pygame.time.Clock()

particle1 = ParticlePrinciple()

PARTICLE_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(PARTICLE_EVENT, 20)

# Font
font = pygame.font.Font("./GameLauncher/assets/games/ClickerGame/assets/fonts/Lato/Lato-Bold.ttf", 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
score = Decimal(0)
click_value = Decimal(1)
auto_click_value = Decimal(0)
auto_click_rate = Decimal(1)
click_value_multi = Decimal(1)
click_rate_multi = Decimal(1)
upgrades = [
    {"num": 1,
    "name": "+1 Per Click",
    "cost": Decimal(85),
    "costcoefficient": Decimal(1.06)},
    {"num": 2,
    "name": "Auto Clicker +0.1",
    "cost": Decimal(40),
    "costcoefficient": Decimal(1.07)},
    {"num": 3,
    "name": "Auto Click Rate +0.1",
    "cost": Decimal(164),
    "costcoefficient": Decimal(1.065)},
    {"num": 4,
    "name": "Double Clicks (X2)",
    "cost": Decimal(300),
    "costcoefficient": Decimal(3.2)},
    {"num": 5,
    "name": "Auto Clicker +1",
    "cost": Decimal(500),
    "costcoefficient": Decimal(1.07)},
    {"num": 6,
    "name": "Double Click Rate (X2)",
    "cost": Decimal(800),
    "costcoefficient": Decimal(4.5)},
    {"num": 7,
    "name": "Auto Clicker +10",
    "cost": Decimal(4500),
    "costcoefficient": Decimal(1.07)},
    {"num": 8,
    "name": "+10 Per Click",
    "cost": Decimal(1000),
    "costcoefficient": Decimal(1.06)},
    {"num": 9,
    "name": "Triple Click Rate (X3)",
    "cost": Decimal(12345),
    "costcoefficient": Decimal(7.5)},
]
upgrade_buttons = []
upgrade_button_width = [300, 360, 400, 380, 360, 440, 360, 320, 460]
upgrade_button_height = [50, 50, 50, 50, 50, 50, 50, 50, 50]
upgrade_button_x = []
for __ in range(1):
    a = 40
    for _ in range(len(upgrade_button_width)):
        upgrade_button_x.append(a)
        a += upgrade_button_width[_] + 20
# upgrade_button_x = [40, 360, 680, 1040, 1420, 1740, 2160, 2480]
(UpgradeButtonColorRed, UpgradeButtonColorGreen, UpgradeButtonColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(UpgradeTargetButtonColorRed, UpgradeTargetButtonColorGreen, UpgradeTargetButtonColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
(UpgradeButtonOutlineColorRed, UpgradeButtonOutlineColorGreen, UpgradeButtonOutlineColorBlue) = (
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
) #(200, 200, 200)
(UpgradeTargetButtonOutlineColorRed, UpgradeTargetButtonOutlineColorGreen, UpgradeTargetButtonOutlineColorBlue) = (
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
) #(0, 0, 0)
Upgrade_Button_X_scroll = 0
Upgrade_Button_X_scroll_vel = 0
# Clicker button
clicker_button_image = pygame.image.load("./GameLauncher/assets/games/ClickerGame/assets/img/copilot.png").convert_alpha()
# clicker_button_rect = clicker_button_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Upgrade button setup
for i, upgrade in enumerate(upgrades):
    x = upgrade_button_x[i]
    y = screen_height - upgrade_button_height[i] - 20
    upgrade_buttons.append(pygame.Rect(x, y, upgrade_button_width[i], upgrade_button_height[i]))


# Game loop
running = True
frames = 0
scale_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scale_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_scale_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_scale_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
start_time = time.time()
delta_time = 0.000001
game_time = -0.000001
GameFPS = 1/delta_time

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

pygame.mixer.init()
def PlayMusic(musNum):
    if musNum == 1:
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.load("./GameLauncher/assets/games/ClickerGame/assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav")
    elif musNum == 2:
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load("./GameLauncher/assets/games/ClickerGame/assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav")
    elif musNum == 3:
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.load("./GameLauncher/assets/games/ClickerGame/assets/audio/Kevin MacLeod - Hep Cats.mp3")
    pygame.mixer.music.play(loops=-1)
PlayMusic(random.randint(1,3))

click_sound = pygame.mixer.Sound("./GameLauncher/assets/games/ClickerGame/assets/audio/Click mouse - Fugitive Simulator - The-Nick-of-Time.wav")
hover_sound = pygame.mixer.Sound("./GameLauncher/assets/games/ClickerGame/assets/audio/251389__deadsillyrabbit__button_hover-wav.wav")
upgrade_sound = pygame.mixer.Sound("./GameLauncher/assets/games/ClickerGame/assets/audio/Upgrade SOund 0001.wav")

Hovering_Buttons = [0,0,0,0,0,0,0,0,0,0]

while running:
    mos_x, mos_y = pygame.mouse.get_pos()
    frames += 1
    (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
    WindowXscale = WindowWidth / screen_width
    WindowYscale = WindowHeight / screen_height
    if WindowXscale < 1 and WindowYscale < 1:
        WindowScale = max(WindowXscale, WindowYscale)
    elif WindowXscale > 1 and WindowYscale > 1:
        WindowScale = min(WindowXscale, WindowYscale)
    else:
        WindowScale = 1.0
    if WindowXscale < 0 and WindowYscale < 0:
        WindowScale2 = min(WindowXscale, WindowYscale)
    elif WindowXscale > 0 and WindowYscale > 0:
        WindowScale2 = min(WindowXscale, WindowYscale)
    else:
        WindowScale2 = 0
    delta_time = (time.time() - start_time) - game_time
    game_time = time.time() - start_time
    if delta_time > 0:
        GameFPS = 1/delta_time
    else:
        GameFPS = math.inf
    if mos_y > WindowHeight - 160:
        if mos_x > WindowWidth/1.1:
            Upgrade_Button_X_scroll_vel -= 60*delta_time
        elif mos_x < WindowWidth - WindowWidth/1.1:
            Upgrade_Button_X_scroll_vel += 60*delta_time
    Upgrade_Button_X_scroll = constrain(Upgrade_Button_X_scroll+Upgrade_Button_X_scroll_vel, screen_width*-1.9, 0)
    Upgrade_Button_X_scroll_vel /= 1.1
    for i, upgrade in enumerate(upgrades):
        x = upgrade_button_x[i] + Upgrade_Button_X_scroll
        y = (screen_height - upgrade_button_height[i]) - 20
        upgrade_buttons[i] = pygame.Rect(x*WindowScale2, y*WindowYscale, upgrade_button_width[i]*WindowScale2, upgrade_button_height[i]*WindowScale2)
        UpgradeButtonColorRed[i] += (UpgradeTargetButtonColorRed[i] - UpgradeButtonColorRed[i])/(0.15/delta_time)
        UpgradeButtonColorGreen[i] += (UpgradeTargetButtonColorGreen[i] - UpgradeButtonColorGreen[i])/(0.15/delta_time)
        UpgradeButtonColorBlue[i] += (UpgradeTargetButtonColorBlue[i] - UpgradeButtonColorBlue[i])/(0.15/delta_time)
        UpgradeButtonOutlineColorRed[i] += (UpgradeTargetButtonOutlineColorRed[i] - UpgradeButtonOutlineColorRed[i])/(0.15/delta_time)
        UpgradeButtonOutlineColorGreen[i] += (UpgradeTargetButtonOutlineColorGreen[i] - UpgradeButtonOutlineColorGreen[i])/(0.15/delta_time)
        UpgradeButtonOutlineColorBlue[i] += (UpgradeTargetButtonOutlineColorBlue[i] - UpgradeButtonOutlineColorBlue[i])/(0.15/delta_time)
        UpgradeButtonColorRed[i] = constrain(UpgradeButtonColorRed[i], 0, 255)
        UpgradeButtonColorGreen[i] = constrain(UpgradeButtonColorGreen[i], 0, 255)
        UpgradeButtonColorBlue[i] = constrain(UpgradeButtonColorBlue[i], 0, 255)
        UpgradeButtonOutlineColorRed[i] = constrain(UpgradeButtonOutlineColorRed[i], 0, 255)
        UpgradeButtonOutlineColorGreen[i] = constrain(UpgradeButtonOutlineColorGreen[i], 0, 255)
        UpgradeButtonOutlineColorBlue[i] = constrain(UpgradeButtonOutlineColorBlue[i], 0, 255)
    x_inside = [0,0,0,0,0,0,0,0,0,0]
    y_inside = [0,0,0,0,0,0,0,0,0,0]
    button_rect_x = [(WindowWidth/1) // 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    button_rect_y = [((WindowHeight/1) // 2) + (math.sin(game_time*5)) * 30 * WindowScale2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # clicker_button_rect = clicker_button_image.get_rect(center=(scale_x[0], scale_y[0]))
    mos_x, mos_y = pygame.mouse.get_pos()
    target_scale_x[0] = 500
    for button_i in range(0, 3):
        if mos_x > button_rect_x[button_i]-(scale_x[button_i]/2)*WindowScale2 and mos_x < button_rect_x[button_i]+(scale_x[button_i]/2)*WindowScale2:
            x_inside[button_i] = 1
        else: x_inside[button_i] = 0
        if mos_y > button_rect_y[button_i]-(scale_y[button_i]/2)*WindowScale2 and mos_y < button_rect_y[button_i]+(scale_y[button_i]/2)*WindowScale2:
            y_inside[button_i] = 1
        else: y_inside[button_i] = 0
        if x_inside[button_i] == 1 and y_inside[button_i] == 1:
            if Hovering_Buttons[button_i] == 0:
                hover_sound.play()
            Hovering_Buttons[button_i] = 1
            if button_i == 0:
                target_scale_x[0] = 550
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        target_scale_x[0] = 450
                        scale_x[0] = constrain(scale_x[0]-40, 200, math.inf)
                        score += Decimal(click_value)*Decimal(random.uniform(0.95, 1.05))*Decimal(click_value_multi)
                        click_sound.play()
                        for i in range(10):
                            particle1.add_particles(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, random.randrange(-180, 180), 4)
            elif button_i == 1:
                pass
        else:
            Hovering_Buttons[button_i] = 0
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i, button in enumerate(upgrade_buttons):
            if button.collidepoint(pygame.mouse.get_pos()):
                UpgradeTargetButtonColorRed[i] = 0
                UpgradeTargetButtonColorGreen[i] = 100
                UpgradeTargetButtonColorBlue[i] = 0
                UpgradeTargetButtonOutlineColorRed[i] = 0
                UpgradeTargetButtonOutlineColorGreen[i] = 255
                UpgradeTargetButtonOutlineColorBlue[i] = 0
            else:
                UpgradeTargetButtonColorRed[i] = 0
                UpgradeTargetButtonColorGreen[i] = 0
                UpgradeTargetButtonColorBlue[i] = 0
                UpgradeTargetButtonOutlineColorRed[i] = 0
                UpgradeTargetButtonOutlineColorGreen[i] = 0
                UpgradeTargetButtonOutlineColorBlue[i] = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(upgrade_buttons):
                if button.collidepoint(event.pos):
                    UpgradeTargetButtonColorRed[i] = 150
                    UpgradeTargetButtonColorGreen[i] = 75
                    UpgradeTargetButtonColorBlue[i] = 0
                    UpgradeTargetButtonOutlineColorRed[i] = 0
                    UpgradeTargetButtonOutlineColorGreen[i] = 128
                    UpgradeTargetButtonOutlineColorBlue[i] = 255
                    if Decimal(score) >= Decimal(upgrades[i]["cost"]):
                        score -= Decimal(upgrades[i]["cost"])
                        upgrades[i]["cost"] *= upgrades[i]["costcoefficient"]
                        if upgrades[i]["num"] == 1:
                            click_value += Decimal(1)
                        elif upgrades[i]["num"] == 2:
                            auto_click_value += Decimal(0.1)
                        elif upgrades[i]["num"] == 3:
                            auto_click_rate += Decimal(0.1)
                        elif upgrades[i]["num"] == 4:
                            click_value_multi *= Decimal(2)
                        elif upgrades[i]["num"] == 5:
                            auto_click_value += Decimal(1)
                        elif upgrades[i]["num"] == 6:
                            click_rate_multi *= Decimal(2)
                        elif upgrades[i]["num"] == 7:
                            auto_click_value += Decimal(10)
                        elif upgrades[i]["num"] == 8:
                            click_value += Decimal(10)
    scale_x[0] += (target_scale_x[0]-scale_x[0])/(0.15/delta_time)
    scale_y[0] = scale_x[0]
    smal = pygame.transform.scale(clicker_button_image, (constrain(scale_x[0]*WindowScale2, 1, math.inf), constrain(scale_y[0]*WindowScale2, 1, math.inf)))
    # Update auto click
    score += Decimal(auto_click_value) * Decimal(auto_click_rate) * Decimal(click_rate_multi) * Decimal(delta_time)


    # Draw screen
    screen.fill((30, 30, 30))
    screen.blit(smal, (button_rect_x[0]-(scale_x[0]/2)*WindowScale2, button_rect_y[0]-(scale_y[0]/2)*WindowScale2))

    # Draw text
    font = pygame.font.Font("./GameLauncher/assets/games/ClickerGame/assets/fonts/Lato/Lato-Bold.ttf", int(24*WindowScale2))
    def draw_text(text, font, color, x, y, align):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "left":
            screen.blit(text_surface, (x, y))
        elif align == "center":
            text_rect.center = (x, y)
            screen.blit(text_surface, text_rect)
    draw_text(f"Clicks: {abbreviate(score, "s", 3, 100000)}", font, WHITE, 10*WindowScale2, 10*WindowScale2, "left")
    draw_text(f"Clicks Per Click: {abbreviate(click_value, "s", 3, 100000)}", font, WHITE, 10*WindowScale2, 40*WindowScale2, "left")
    draw_text(f"Click Value Multiplier: x{abbreviate(click_value_multi, "s", 3, 100000)}", font, WHITE, 10*WindowScale2, 70*WindowScale2, "left")
    draw_text(f"Clicks Per Second: {abbreviate(auto_click_value, "s", 3, 100000)}/s", font, WHITE, 10*WindowScale2, 100*WindowScale2, "left")
    if delta_time > 0:
        draw_text(f"FPS: {Decimal(1/delta_time):.2f}", font, WHITE, 10*WindowScale2, 130*WindowScale2, "left")
    else:
        draw_text(f"FPS: INFINITY", font, WHITE, 10*WindowScale2, 130*WindowScale2, "left")
    draw_text(f"Seconds Per Second: {abbreviate(auto_click_rate, "s", 3, 1000)}/s", font, WHITE, 10*WindowScale2, 160*WindowScale2, "left")
    draw_text(f"Seconds Per Seconds Per Second: {abbreviate(click_rate_multi, "s", 3, 1000)}/s", font, WHITE, 10*WindowScale2, 190*WindowScale2, "left")
    draw_text(f"Total Clicks Per Second: {abbreviate(auto_click_value * auto_click_rate * click_rate_multi, "s", 3, 1000)}/s", font, WHITE, 10*WindowScale2, 220*WindowScale2, "left")
    draw_text(f"Total Clicks Per Click: {abbreviate(click_value * click_value_multi, "s", 3, 100000)}", font, WHITE, 10*WindowScale2, 250*WindowScale2, "left")

    # Draw upgrade buttons
    for i, button in enumerate(upgrade_buttons):
        upgx = upgrade_button_x[i] + Upgrade_Button_X_scroll
        upgy = (screen_height - upgrade_button_height[i]) - 20
        upgrade_buttons[i] = pygame.Rect(upgx*WindowScale2, upgy*WindowYscale, upgrade_button_width[i]*WindowScale2, upgrade_button_height[i]*WindowScale2)
        pygame.draw.rect(screen, (UpgradeButtonOutlineColorRed[i], UpgradeButtonOutlineColorGreen[i], UpgradeButtonOutlineColorBlue[i]), (upgx*WindowScale2 - 5*WindowScale2, upgy*WindowYscale - 5*WindowScale2, upgrade_button_width[i]*WindowScale2 + 10*WindowScale2, upgrade_button_height[i]*WindowScale2 + 10*WindowScale2), 30)
        pygame.draw.rect(screen, (UpgradeButtonColorRed[i], UpgradeButtonColorGreen[i], UpgradeButtonColorBlue[i]), button)
        draw_text(f"{upgrades[i]['name']} - {abbreviate(upgrades[i]['cost'], "s", 3, 10000)}", font, WHITE, upgx*WindowScale2 + upgrade_button_width[i]*WindowScale2/2, upgy*WindowYscale + upgrade_button_height[i]*WindowScale2/2, "center")

    # Update display
    particle1.emit()
    pygame.display.flip()
    pygame.display.update()
    # clock.tick(24)

# Quit Pygame
pygame.quit()

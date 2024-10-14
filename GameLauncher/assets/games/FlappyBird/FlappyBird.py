# Import Module
import random
import sys
import pygame
from pygame.locals import *
from pygame import mixer
import time
import math
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import *
from PyQt5.QtGui import QColor

class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        super(Settings, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup1(), 0, 0)
        grid.addWidget(self.createExampleGroup2(), 1, 0)
        self.setLayout(grid)

        self.setWindowTitle("Settings")
        self.resize(400, 300)
        self.setStyleSheet("Settings{background: rgb(0, 200, 0)}")
        style = {
            "sub-page.color": QColor(70, 23, 180)
        }

    def createExampleGroup1(self):
        groupBox = QGroupBox("Music")

        radio1 = QRadioButton("&Music On")
        radio2 = QRadioButton("&Music Off")

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)
        slider.setValue(100)

        radio1.setChecked(True)
        radio2.setChecked(False)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox
    def createExampleGroup2(self):
        groupBox = QGroupBox("SFX")
        radio3 = QRadioButton("&SFX On")
        radio4 = QRadioButton("&SFX Off")
        
        slider2 = QSlider(Qt.Horizontal)
        slider2.setFocusPolicy(Qt.StrongFocus)
        slider2.setTickPosition(QSlider.TicksBothSides)
        slider2.setTickInterval(10)
        slider2.setSingleStep(1)
        slider2.setValue(100)

        radio3.setChecked(True)
        radio4.setChecked(False)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(radio3)
        vbox2.addWidget(radio4)
        vbox2.addWidget(slider2)
        vbox2.addStretch(1)
        groupBox.setLayout(vbox2)

        return groupBox
QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
app = QApplication(sys.argv)
settings = Settings()

def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

# All the Game Variables
screenwidth = 1024
screenheight = 1024

# Set height and width of window
window = pygame.display.set_mode((screenwidth, screenheight),  pygame.RESIZABLE)
elevation = screenheight * 0.8
game_images = {}
framespersecond = 24
pipeimage = 'GameLauncher/assets/games/FlappyBird/assets/img/pipe.png'
background_image = "GameLauncher/assets/games/FlappyBird/assets/img/Background6.png"
birbNum = random.randint(0, 1)
# BeegBirb = pygame.image.load(birdplayer_image).convert_alpha()
if birbNum == 0:
    birdplayer_image = 'GameLauncher/assets/games/FlappyBird/assets/img/bird1gif.png'
    BeegBirb = pygame.transform.scale(pygame.image.load(birdplayer_image).convert_alpha(), (32, 32))
else:
    birdplayer_image = 'GameLauncher/assets/games/FlappyBird/assets/img/Amon.png'
    BeegBirb = pygame.transform.scale(pygame.image.load(birdplayer_image).convert_alpha(), (56, 50))
sealevel_image = 'GameLauncher/assets/games/FlappyBird/assets/img/base.png'
smalbg = pygame.transform.scale(pygame.image.load(background_image).convert_alpha(), (1024, 1024))

def flappygame():
    (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
    start_time = time.time()
    delta_time = 0.0001
    game_time = -0.0001
    your_score = 0
    horizontal = int(screenwidth / 5)
    vertical = int(screenheight / 2)
    ground = -128
    mytempheight = 100
    pipe_time = 2

    # Generating two pipes for blitting on window
    first_pipe = createPipe()
    second_pipe = createPipe()

    # List containing lower pipes
    down_pipes = [
        {'x': WindowWidth+300-mytempheight, 'y': first_pipe[1]['y']},
        {'x': WindowWidth+300-mytempheight+(WindowWidth/2), 'y': second_pipe[1]['y']},
    ]

    # List containing upper pipes
    up_pipes = [
        {'x': WindowWidth+300-mytempheight, 'y': first_pipe[0]['y']},
        {'x': WindowWidth+300-mytempheight+(WindowWidth/2), 'y': second_pipe[0]['y']},
    ]

    # Pipe velocity along x
    pipeVelX = -4

    # Bird velocity
    bird_velocity_y = 0
    bird_Max_Vel_Y = 10

    bird_flap_velocity = -1
    bird_flapped = False
    bird_down_velocity_y = bird_flap_velocity*-2
    bird_down = 0
    bird_down_down = 0

    frames = 0
    ScrollX = [0, 0]
    while True:
        (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
        xscale = WindowWidth / screenwidth
        yscale = WindowHeight / screenheight
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
        delta_time = (time.time() - start_time) - game_time
        game_time = time.time() - start_time
        bird_down -= 1
        frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                bird_down_down = 0
                if vertical > 0:
                    bird_velocity_y = bird_flap_velocity
                    flapSound = mixer.Sound("GameLauncher/assets/games/FlappyBird/assets/audio/sfx_wing.wav")
                    flapSound.play()
                    bird_flapped = True
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN):
                bird_velocity_y = bird_down_velocity_y
                bird_down = 0.14/delta_time
                bird_down_down = 1
        
        # This function will return true if the flappybird is crashed
        game_over = isGameOver(horizontal, vertical, up_pipes, down_pipes)
        if game_over:
            DedSound = mixer.Sound("GameLauncher/assets/games/FlappyBird/assets/audio/john hurt.wav")
            DedSound.play()
            return
        
        # Check for your_score
        playerMidPos = horizontal + BeegBirb.get_width()/2
        for pipe in up_pipes:
            pipeMidPos = pipe['x'] + game_images['pipeimage'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos - pipeVelX:
                your_score += 1
                ScoreSound = mixer.Sound("GameLauncher/assets/games/FlappyBird/assets/audio/Discord notification - sound effect.wav")
                ScoreSound.play()
                print(f"Your score is {your_score}.")

        if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
            bird_velocity_y *= .09**delta_time
            bird_velocity_y += 3*delta_time
        if bird_down_down == 1:
            if bird_down > 0:
                bird_velocity_y = bird_down_velocity_y
            else:
                bird_velocity_y = 0
                bird_down_down = 0
        
        if bird_flapped:
            bird_flapped = False
        playerHeight = BeegBirb.get_height()
        vertical += min(bird_velocity_y * delta_time * 666, elevation - vertical - playerHeight)
        
        # Move pipes to the left
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            upperPipe['x'] += -240*delta_time
            lowerPipe['x'] += -240*delta_time
            pipeVelX = -240*delta_time
        
        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if game_time > pipe_time:
            pipe_time += random.uniform(2, 3.1)
            newpipe = createPipe()
            up_pipes.append(newpipe[0])
            down_pipes.append(newpipe[1])
            
        
        # If the pipe is out of the screen, remove it.
        if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
            up_pipes.pop(0)
            down_pipes.pop(0)
        
        # Lets blit our game images now
        bg_width = 1024
        ground -= 240*delta_time 
        if ground <= -512:
            ground = -128
        tiles = math.ceil(WindowWidth / bg_width) + 10
        ScrollX[0] -= 120*delta_time
        if abs(ScrollX[0]) > bg_width: ScrollX[0] = 0
        for i in range(0, tiles):
            window.blit(smalbg, (i*bg_width+ScrollX[0],0))
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            window.blit(game_images['pipeimage'][0], (upperPipe['x'], upperPipe['y']))
            window.blit(game_images['pipeimage'][1], (lowerPipe['x'], lowerPipe['y']))
        window.blit(game_images['sea_level'], (ground, elevation))
        window.blit(BeegBirb, (horizontal, vertical))
        
        # Fetching the digits of score.
        numbers = [int(x) for x in list(str(your_score))]
        width = 0

        # Finding the width of score images from numbers.
        for num in numbers:
            width += game_images['scoreimages'][num].get_width()
        Xoffset = (WindowWidth - width)/1.1

        # Blitting the images on the window
        for num in numbers:
            window.blit(pygame.transform.scale(game_images['scoreimages'][num], (xscale * game_images['scoreimages'][num].get_width(), xscale * game_images['scoreimages'][num].get_height())), (Xoffset, WindowWidth*0.02))
            Xoffset += pygame.transform.scale(game_images['scoreimages'][num], (xscale * game_images['scoreimages'][num].get_width(), xscale * game_images['scoreimages'][num].get_height())).get_width()
        
        # Refreshing the game window and displaying the score.   
        pygame.display.update()
        pygame.display.flip()
        #Clock.tick(24)

def isGameOver(horizontal, vertical, up_pipes, down_pipes):
    if vertical > elevation - (((birbNum == 1) * 66) + ((birbNum == 0) * 40)) or vertical < 0:
        return True
    
    for pipe in up_pipes:
        pipeHeight = game_images['pipeimage'][0].get_height()
        if (vertical < pipeHeight + pipe['y'] and \
            abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
            return True
        for pipe in down_pipes:
            if (vertical + BeegBirb.get_height() > pipe['y']) and\
                abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
                return True
        return False
    
def createPipe():
    (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
    offset = WindowHeight/random.randint(3, 6)
    pipeHeight = game_images['pipeimage'][0].get_height()
    y2 = offset + \
        constrain(random.randint(0, int(constrain(WindowHeight/1.69, 2, math.inf) - 1.2 * offset)), 2, math.inf)
    pipeX = WindowWidth + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        # Upper Pipe
        {'x': pipeX, 'y': -y1},

        # Lower Pipe
        {'x': pipeX, 'y': y2}
    ]
    return pipe

# Program where the game starts
# For initializing modules of pygame library
pygame.init()
Clock = pygame.time.Clock()

# Sets the title on top of game window
pygame.display.set_caption("Morphing Under Night Armor - Flappy Bird")

# Load all the images which we will use in the game

# Images for displaying the score

game_images['sea_level'] = pygame.image.load(sealevel_image).convert_alpha()
game_images['background'] = pygame.image.load(background_image).convert_alpha()
game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(pipeimage).convert_alpha(), 180), pygame.image.load(pipeimage).convert_alpha())

print("WELCOME TO FLAPPY BIRD!")
print("Press space or up to start the game.")
print("Computer required.")
# Background Sound
mus = random.randint(1,2)
if mus == 1:
    mixer.music.load("GameLauncher/assets/games/FlappyBird/assets/audio/uplift - awesome HIGH QUALITY.wav")
elif mus == 2:
    mixer.music.load("GameLauncher/assets/games/FlappyBird/assets/audio/uplift - lols HIGH QUALITY.wav")
mixer.music.play(-1)

# Here starts the main game
settings.show()
while True:
    # Sets the coordinates of flappy bird
    horizontal = int(screenwidth/5)
    vertical = int(screenheight - BeegBirb.get_height())/2
    ground = -128
    while True:
        (WindowWidth, WindowHeight) = pygame.display.get_surface().get_size()
        if random.randint(0, 1) == 1:
            game_images['scoreimages'] = (
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/0.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/1.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/2.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/3.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/4.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/5.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/6.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/7.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/8.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/9.png').convert_alpha()
            )
        else:
            game_images['scoreimages'] = (
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_0.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_1.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_2.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_3.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_4.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_5.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_6.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_7.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_8.png').convert_alpha(),
                pygame.image.load('GameLauncher/assets/games/FlappyBird/assets/img/glitched_9.png').convert_alpha()
            )
        for event in pygame.event.get():
            # If user clicks on cross button, close the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # If the user presses space or up key, start the game for them
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                flapSound = mixer.Sound("GameLauncher/assets/games/FlappyBird/assets/audio/sfx_wing.wav")
                flapSound.play()
                flappygame()
            # If user doesn't press anykey Nothing happen
            else:
                #game_images['background']
                ScrollX = [0, 0]
                bg_width = 1024
                tiles = math.ceil(WindowWidth / bg_width) + 10
                if abs(ScrollX[0]) > bg_width: ScrollX[0] = 0
                for i in range(0, tiles):
                    window.blit(smalbg, (i*bg_width+ScrollX[0],0))
                window.blit(BeegBirb, (horizontal, vertical))
                window.blit(game_images['sea_level'], (ground, elevation))
                pygame.display.update()
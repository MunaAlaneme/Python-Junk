# Importing libraries
import pygame
import time
import random
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import PyQt5
from PyQt5 import *

App1 = QApplication([0,0])

snake_speed = 0
def getTextInput(title, message):
    answer = QInputDialog.getText(None, title, message)
    if answer[1]:
        print(answer[0])
        return answer[0]
    else:
        return None
game_level = getTextInput("Game mode", "Enter m for medium. h for hard. e for easy. i for impossible. n for nightmare.")


if game_level == "m":
    snake_speed = 10
elif game_level == "e":
    snake_speed = 5
elif game_level == "h":
    snake_speed = 15
elif game_level == "i":
    snake_speed = 24
elif game_level == "n":
    snake_speed = 40

# Window size
window_x = 1600
window_y = 900
# The ratio is 16:9

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialization of pygame
pygame.init()
pointSound = pygame.mixer.Sound("GameLauncher/assets/games/SnakeGame/assets/audio/Discord notification - sound effect.wav")
deadSound = pygame.mixer.Sound("GameLauncher/assets/games/SnakeGame/assets/audio/sound (1).wav")

# Initialization of game window
pygame.display.set_caption("Morphing Under Night Armor - Snake")
game_window = pygame.display.set_mode((window_x, window_y), pygame.RESIZABLE)

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Defining snake default position
snake_position = [snake_speed*5, snake_speed*2]

# Defining first 4 blocks of snake body

snake_body = [
    [snake_speed*5, snake_speed*2],
    [snake_speed*4, snake_speed*2],
    [snake_speed*3, snake_speed*2],
    [snake_speed*2, snake_speed*2],
]

# Fruit position
fruit_position = [random.randint(1, (window_x//snake_speed)) * snake_speed, random.randint(1, (window_y//snake_speed)) * snake_speed]
fruit_spawn = True

# Setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Display score function
def show_score(choice, color, font, size):
    # Create font object score_font
    score_font = pygame.font.SysFont(font, size)

    # Create the display surface object score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # Create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # Displaying text
    game_window.blit(score_surface, score_rect)
def blit_text(surface, text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()] # 2D array where each row is a list of words.
    space = font.size(' ')[0] # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0] # Reset the x.
                y += word_height # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0] # Reset the x.
        y += word_height # Start on new row.
info_text = """Use arrow keys to move.\nMusic by Scratch User uplift\nSounds by Discord and Chiptone by SFB Games\nMade by MunaAlaneme\nTutorial by GeeksForGeeks, YouTuber sentdex, and pythonprogramming.net"""
def show_info(choice, color, font, size):
    # Create font object info_font
    info_font = pygame.font.SysFont(font, size)

    # Create the display surface object info_surface
    info_text = """Use arrow keys to move.\nMusic by Scratch User uplift\nSounds by Discord and Chiptone by SFB Games\nMade by MunaAlaneme\nTutorial by GeeksForGeeks, YouTuber sentdex, and pythonprogramming.net"""
    info_surface = info_font.render(info_text, True, color)

    # Create a rectangular object for the text surface object
    info_rect = info_surface.get_rect()
    info_rect.midtop = (window_x/2, window_y/1.5)

    # Displaying text
    game_window.blit(info_surface, info_rect)

# Game over function
def game_over():
    # Creating font object my_font
    my_font = pygame.font.SysFont('Dosis', 75)

    # Creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score: ' + str(score), True, red)

    # Creating a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # Setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # Blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # After 10 seconds we will quit the program
    pygame.time.delay(10000)

    # Deactivate the pygame library
    pygame.quit()
    
    # Quit the program
    quit()

# Main Function
time.sleep(1)
m = random.randint(1,2)
if m == 1:
    pygame.mixer.music.load("GameLauncher/assets/games/SnakeGame/assets/audio/uplift - awesome HIGH QUALITY.wav")
elif m == 2:
    pygame.mixer.music.load("GameLauncher/assets/games/SnakeGame/assets/audio/uplift - lols HIGH QUALITY.wav")
pygame.mixer.music.play(-1)
running = True
while running:
    # If two keys pressed simutaneously we don't want snake to move in two directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= snake_speed
    if direction == 'DOWN':
        snake_position[1] += snake_speed
    if direction == 'LEFT':
        snake_position[0] -= snake_speed
    if direction == 'RIGHT':
        snake_position[0] += snake_speed

    # Snake body growing mechanism if fruits and snakes collide then scores will be incremented by 1
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        pygame.mixer.Sound.play(pointSound)
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randint(1, (window_x//snake_speed)) * snake_speed, random.randint(1, (window_y//snake_speed)) * snake_speed]

    fruit_spawn = True
    game_window.fill((0,0,0))

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], snake_speed, snake_speed))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], snake_speed, snake_speed))

    # Game Over Conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - snake_speed or snake_position[1] < 0 or snake_position[1] > window_y - snake_speed:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(deadSound)
        game_over()
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(deadSound)
            game_over()
    
    # Displaying score continously
    info_font = pygame.font.SysFont('Dosis', 30)
    show_score(1, white, 'Dosis', 40)
    blit_text(game_window, info_text, (1/window_x, window_y/1.3), info_font, green)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second / Refresh Rate
    fps.tick(snake_speed)
    
    # Handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'  

# https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
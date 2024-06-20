import pygame
import sys
from decimal import *
import random

print(Decimal.__abs__(Decimal(33)))

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
FONT_SIZE = 24

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")

# Load sounds and music
def PlayMusic(musNum):
    if musNum == 1:
        pygame.mixer.music.load("./GameLauncher/assets/games/ClickerGame/assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav")
    elif musNum == 2:
        pygame.mixer.music.load("./GameLauncher/assets/games/ClickerGame/assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav")
    pygame.mixer.music.play(-1)
PlayMusic(random.randint(1,2))
pygame.mixer.music.set_volume(0.5)
click_sound = pygame.mixer.Sound("./GameLauncher/assets/games/ClickerGame/assets/audio/Click mouse - Fugitive Simulator - The-Nick-of-Time.wav")

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
score = 0
click_multiplier = 1
auto_clicker_level = 0

# Button
button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 100)

# Settings
music_on = True
sound_on = True

# Main game loop
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)  # Loop background music

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += click_multiplier
                click_sound.play()

    # Update game logic here (e.g., auto-clickers, upgrades, etc.)

    # Draw UI
    screen.fill(WHITE)
    pygame.draw.rect(screen, (0, 128, 255), button_rect)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Draw settings
    settings_text = font.render("Settings", True, (0, 0, 0))
    screen.blit(settings_text, (WIDTH - 100, 10))
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH - 100, 40, 80, 30))
    pygame.draw.rect(screen, (255, 0, 0) if not music_on else (0, 255, 0), (WIDTH - 90, 45, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0) if not sound_on else (0, 255, 0), (WIDTH - 60, 45, 20, 20))

    pygame.display.flip()
    clock.tick(FPS)

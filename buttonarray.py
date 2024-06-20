import math
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BUTTON_WIDTH = (120, 140, 160, 180, 200, 320, 100, 100)
(BUTTON_X_POS, BUTTON_Y_POS) = ([20, 160, 320, 500, 20, 240, 580, 700], ((SCREEN_HEIGHT // 2) - 35, (SCREEN_HEIGHT // 2) - 35, (SCREEN_HEIGHT // 2) - 35, (SCREEN_HEIGHT // 2) - 35, (SCREEN_HEIGHT // 2) + 35, (SCREEN_HEIGHT // 2) + 35, (SCREEN_HEIGHT // 2) + 35, (SCREEN_HEIGHT // 2) + 35))

BUTTON_HEIGHT = 35
BUTTON_GAP_Y = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
(TargetButtonColorRed, TargetButtonColorGreen, TargetButtonColorBlue) = ([200, 200, 200, 200, 200, 200, 200, 200], [200, 200, 200, 200, 200, 200, 200, 200], [200, 200, 200, 200, 200, 200, 200, 200]) #(200, 200, 200)
(ButtonColorRed, ButtonColorGreen, ButtonColorBlue) = ([0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]) #(0, 0, 0)
GameNames = ("Thing 1", "Monkey 2", "Meat 3", "AAAAA 4", "HAHAHAHA 5", "no it doesn't make sense 6", "a 7", "8")

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Functional Button Array with Text in Pygame')

# Create a font for the button text
font = pygame.font.Font(None, 36)

# Create a list to store buttons
buttons = []

# Create buttons and add them to the list

for i in range(8):
    button_rect = pygame.Rect(
        BUTTON_X_POS[i],
        BUTTON_Y_POS[i],
        BUTTON_WIDTH[i],
        BUTTON_HEIGHT
    )
    buttons.append(button_rect)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if any button is clicked
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    print(f"Button {i + 1} clicked!")

    # Draw background
    screen.fill(WHITE)

    # Draw buttons and text
    for i, button in enumerate(buttons):
        ButtonColorRed[i] += (TargetButtonColorRed[i] - ButtonColorRed[i])/20
        ButtonColorGreen[i] += (TargetButtonColorGreen[i] - ButtonColorGreen[i])/20
        ButtonColorBlue[i] += (TargetButtonColorBlue[i] - ButtonColorBlue[i])/20
        pygame.draw.rect(screen, (ButtonColorRed[i], ButtonColorGreen[i], ButtonColorBlue[i]), button)
        pygame.draw.rect(screen, BLACK, button, 2)

        # Highlight the button when the mouse is over it
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, GREEN, button, 2)
            TargetButtonColorRed[i] = 0
            TargetButtonColorGreen[i] = 255
            TargetButtonColorBlue[i] = 0
        else:
            TargetButtonColorRed[i] = 200
            TargetButtonColorGreen[i] = 200
            TargetButtonColorBlue[i] = 200

        # Render and draw centered text on the button
        text = font.render(GameNames[i], True, BLACK)
        text_rect = text.get_rect(center=button.center)
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(240)

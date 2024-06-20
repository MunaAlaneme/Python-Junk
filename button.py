import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 80
BUTTON_COLOR_RED = 52
BUTTON_COLOR_GREEN = 152
BUTTON_COLOR_BLUE = 219
BUTTON_HIGHLIGHT_COLOR_RED = 41
BUTTON_HIGHLIGHT_COLOR_GREEN = 128
BUTTON_HIGHLIGHT_COLOR_BLUE = 185
TEXT_COLOR = (255, 255, 255)
BUTTON_TEXT = "Cool Button"

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cool Pygame Button")

# Fonts
font = pygame.font.Font(None, 36)

class CoolButton:
    def __init__(self, x, y, width, height, text, text_color, button_color, button_color_red, button_color_green, button_color_blue, highlight_color, highlight_color_red, highlight_color_green, highlight_color_blue):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color_red = button_color_red
        self.button_color_green = button_color_green
        self.button_color_blue = button_color_blue
        self.highlight_color_red = highlight_color_red
        self.highlight_color_green = highlight_color_green
        self.highlight_color_blue = highlight_color_blue
        self.button_color = button_color
        self.highlight_color = highlight_color
        self.highlighted = False
        self.clicked = False
        self.clicked_animation = 0

    def draw(self, screen):
        if self.highlighted:
            pygame.draw.rect(screen, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        if self.clicked:
            self.clicked_animation += 1
            if self.clicked_animation >= 10:
                self.clicked_animation = 0
                self.clicked = False
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)

    def is_hovered(self, pos):
        if self.rect.collidepoint(pos):
            self.highlighted = True
        else:
            self.highlighted = False

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.clicked = True
            return True
        return False

# Create a cool button instance
button = CoolButton(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_TEXT, TEXT_COLOR, (BUTTON_COLOR_RED, BUTTON_COLOR_GREEN, BUTTON_COLOR_BLUE), BUTTON_COLOR_RED, BUTTON_COLOR_GREEN, BUTTON_COLOR_BLUE, (BUTTON_HIGHLIGHT_COLOR_RED, BUTTON_HIGHLIGHT_COLOR_GREEN, BUTTON_HIGHLIGHT_COLOR_BLUE), BUTTON_HIGHLIGHT_COLOR_RED, BUTTON_HIGHLIGHT_COLOR_GREEN, BUTTON_HIGHLIGHT_COLOR_BLUE)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            button.is_hovered(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                print("Button clicked!")

    screen.fill((255, 255, 255))
    button.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
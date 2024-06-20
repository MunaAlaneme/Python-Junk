import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 24
ITEM_HEIGHT = FONT_SIZE + 5
ITEMS = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]

# Customizable parameters
x_position = SCREEN_WIDTH // 2
y_position = SCREEN_HEIGHT // 2
velocity = 30
menu_width = 200
menu_height = SCREEN_HEIGHT
clipping_box = pygame.Rect(x_position - menu_width // 2, y_position - menu_height // 2, menu_width, menu_height)

# Initialize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vertical Scroll Menu")

font = pygame.font.Font(None, FONT_SIZE)
scroll = 0

def render_menu(scroll):
    screen.fill(BLACK)
    for i, item in enumerate(ITEMS):
        text = font.render(item, True, WHITE)
        text_rect = text.get_rect(center=(x_position, i * ITEM_HEIGHT - scroll + y_position))
        if text_rect.colliderect(clipping_box):
            screen.blit(text, text_rect)

def handle_scroll(scroll):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scroll = max(0, scroll - velocity)
            elif event.key == pygame.K_DOWN:
                scroll = min((len(ITEMS) - 1) * ITEM_HEIGHT, scroll + velocity)
    return scroll

# Main loop
while True:
    scroll = handle_scroll(scroll)
    render_menu(scroll)
    pygame.draw.rect(screen, WHITE, clipping_box, 2)  # Draw the clipping box
    pygame.display.flip()
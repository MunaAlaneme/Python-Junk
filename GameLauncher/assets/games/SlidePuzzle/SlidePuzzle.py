# Import modules
import pygame
import random
import pyautogui
from pygame.locals import *

class Tiles:
    # Main method for initializing different variables
    def __init__(self, screen, start_position_x, start_position_y, num, mat_pos_x, mat_pos_y):
        self.color = (0, 255, 0)
        # complete screen
        self.screen = screen
        # screen(x)
        self.start_pos_x = start_position_x
        # screen(y)
        self.start_pos_y = start_position_y
        # total nums
        self.num = num
        # width of each tile
        self.width = tile_width
        # depth of each tile(shadow)
        self.depth = tile_depth
        # tile selected false
        self.selected = False
        # matrix alignment from screen w.r.t x coordinate
        self.position_x = mat_pos_x
        # matrix alignment from screen w.r.t y coordinate
        self.position_y = mat_pos_y
        # tile movable false in its initial state
        self.movable = False

    # Draw tiles
    def draw_tyle(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.start_pos_x, self.start_pos_y, self.width, self.depth))
        numb = font.render(str(self.num), True, (125, 55, 100))
        screen.blit(numb, (self.start_pos_x + int(page_width * 0.15/rows), self.start_pos_y + 10))
    
    # Mouse hover change the color of tiles
    def mouse_hover(self, x_m_motion, y_m_motion):
        if x_m_motion > self.start_pos_x and x_m_motion < self.start_pos_x + self.width and y_m_motion > self.start_pos_y and y_m_motion < self.start_pos_y + self.depth:
            self.color = (255, 255, 255)
        else:
            self.color = (255, 165, 0)
    
    # When mouse clicks check if a tile is selected or not
    def mouse_click(self, x_m_click, y_m_click):
        if x_m_click > self.start_pos_x and x_m_click < self.start_pos_x + self.width and y_m_click > self.start_pos_y and y_m_click < self.start_pos_y + self.depth:
            self.selected = True
        else:
            self.selected = False
    
    # When mouse click released unselect the tile by setting False
    def mouse_click_release(self, x_m_click_rel, y_m_click_rel):
        if x_m_click_rel > 0 and y_m_click_rel > 0:
            self.selected = False
    
    # Move the tile (i.e hover)
    def move_tyle(self, x_m_motion, y_m_motion):
        self.start_pos_x2 = x_m_motion - int(page_width * 0.15/rows)
        self.start_pos_y2 = y_m_motion - int(page_width * 0.15/rows)        
        self.start_pos_x += (self.start_pos_x2 - self.start_pos_x) / 9
        self.start_pos_y += (self.start_pos_y2 - self.start_pos_y) / 9

# Create tiles w.r.t to number of tiles available
def create_tyles():
    i = 1
    while i <= tile_count:
        r = random.randint(1, tile_count)
        if r not in tile_no:
            tile_no.append(r)
            i += 1
    tile_no.append("")
    k = 0
    for i in range(0, rows):
        for j in range (0, cols):
            if (i == rows - 1) and (j == cols - 1):
                pass
            else:
                t = Tiles(screen, tile_print_position[(i, j)][0], tile_print_position[(i, j)][1], tile_no[k], i, j)
                tiles.append(t)
            matrix[i][j] = tile_no[k]
            k += 1
    check_mobility()

# Check if the tile can be places on the required position where the player is trying to move the tile
def check_mobility():
    for i in range(tile_count):
        tile = tiles[i]
        row_index = tile.position_x
        col_index = tile.position_y
        adjacent_cells = []
        adjacent_cells.append([row_index-1, col_index, False])
        adjacent_cells.append([row_index+1, col_index, False])
        adjacent_cells.append([row_index, col_index-1, False])
        adjacent_cells.append([row_index, col_index+1, False])
        for i in range(len(adjacent_cells)):
            if (adjacent_cells[i][0] >= 0 and adjacent_cells[i][0] < rows) and (adjacent_cells[i][1] >= 0 and adjacent_cells[i][1] < cols):
                adjacent_cells[i][2] = True
        for j in range(len(adjacent_cells)):
            if adjacent_cells[j][2]:
                adj_cell_row = adjacent_cells[j][0]
                adj_cell_col = adjacent_cells[j][1]
                for k in range(tile_count):
                    if adj_cell_row == tiles[k].position_x and adj_cell_col == tiles[k].position_y:
                        adjacent_cells[j][2] = False
                false_count = 0
                for m in range(len(adjacent_cells)):
                    if adjacent_cells[m][2]:
                        tile.movable = True
                        break
                    else:
                        false_count += 1
                
                if false_count == 4:
                    tile.movable = False
# If after iterating the matrix the string we get is 12345678_ then the player has won("Game Over")
def isGameOver():
    global game_over, game_over_banner
    allcelldata = ""
    for i in range(rows):
        for j in range(cols):
            allcelldata = allcelldata + str(matrix[i][j])
    if allcelldata == "12345678 ":
        game_over = True
        game_over_banner = "Game Over"

        print ("Game Over")

        for i in range(tile_count):
            tiles[i].movable = False
            tiles[i].selected - False
# Window dimension
page_width, page_depth = pyautogui.size()
page_width = int(page_width * 0.95)
page_depth = int(page_depth * 0.95)
# Tile dimensions
tiles = []
rows, cols = (3, 3)
tile_width = int(page_width * 0.45/rows)
tile_depth = int(page_depth * 0.45/cols)
# Number of rows and columns i.e puzzle size
tile_count = rows * cols - 1 # How many tiles should be created
matrix = [["" for i in range(cols)] for j in range(rows)]
tile_no = []
tile_print_position = {
    (0,0): (100, 50),
    (0,1): (100 + int(page_width * 0.5/rows), 50),
    (0,2): (100 + 2*(int(page_width * 0.5/cols)), 50),
    (1,0): (100, 50 + int(page_depth * 0.5/cols)),
    (1,1): (100 + int(page_width * 0.5/rows), 50 + int(page_depth * 0.5/cols)),
    (1,2): (100 + 2*(int(page_width * 0.5/cols)), 50 + int(page_depth * 0.5/cols)),
    (2,0): (100, 50 + 2*(int(page_depth * 0.5/cols))),
    (2,1): (100 + int(page_width * 0.5/rows), 50 + 2*(int(page_depth * 0.5/cols))),
    (2,2): (100 + 2*(int(page_width * 0.5/cols)), 50 + 2*(int(page_depth * 0.5/cols)))  
}

# Initial values of variables
mouse_press = False
x_m_click, y_m_click = 0, 0
x_m_click_rel, y_m_click_rel = 0, 0
game_over = False
game_over_banner = ""

# Initialize pygame and set the caption
pygame.init()
game_over_font = pygame.font.Font("Fonts/Dosis/static/Dosis-Bold.ttf", 70)
move_count = 0
move_count_banner = "Moves: "
move_count_font = pygame.font.Font("Fonts/Dosis/static/Dosis-Bold.ttf", 40)
screen = pygame.display.set_mode((page_width, page_depth))
pygame.display.set_caption("Morphing Under Night Armor - Slide Game")
font = pygame.font.Font("Fonts/Dosis/static/Dosis-Bold.ttf", 100)
# Creation of tiles in the puzzle
create_tyles()

# Background Sound
mus = random.randint(1,2)
if mus == 1:
    pygame.mixer.music.load("./GameLauncher/assets/games/SlidePuzzle/assets/audio/uplift - awesome HIGH QUALITY.wav")
elif mus == 2:
    pygame.mixer.music.load("./GameLauncher/assets/games/SlidePuzzle/assets/audio/uplift - lols HIGH QUALITY.wav")
pygame.mixer.music.play(-1)

running = True
while running:
    screen.fill((0, 0, 0)) # fill with black color
    # Start drawing the gui board of sliding puzzle
    pygame.draw.rect(screen, (165, 42, 42), pygame.Rect(95, 45, tile_width*3.6, tile_depth*3.6))
    game_over_print = game_over_font.render(game_over_banner, True, (255, 255, 0))
    # blit() will take that rectangular Surface and put it on top of the screen.
    screen.blit(game_over_print, (950, 100))

    # Render the move count with the use of str
    if move_count == 0:
        move_count_render = move_count_font.render(move_count_banner + "0", True, (0, 255, 0))
    else:
        move_count_render = move_count_font.render(move_count_banner + str(move_count), True, (0, 255, 0))
    screen.blit(move_count_render, (1050, 200))

    # Get events from the queue.
    for event in pygame.event.get():
        # if its quite operation then exit the while loop
        if event.type == pygame.QUIT:
            running = False
        # if mouse click are detected then find (x,y) and then pass them to mouse_hover method
        if event.type == pygame.MOUSEMOTION:
            x_m_motion, y_m_motion = pygame.mouse.get_pos()
            for i in range(tile_count):
                tiles[i].mouse_hover(x_m_motion, y_m_motion)
            # if the tile is selected & mouse is pressed then pass the coords to move_tyle method
            for i in range(tile_count):
                if tiles[i].selected and mouse_press:
                    tiles[i].move_tyle(x_m_motion, y_m_motion)
        # Moving tile downwards
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = True
            x_m_click, y_m_click = pygame.mouse.get_pos()
            for i in range(tile_count):
                tiles[i].mouse_click(x_m_click, y_m_click)
        # Moving tile upwards
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_press = False
            x_m_click_rel, y_m_click_rel = pygame.mouse.get_pos()
            x_m_click, y_m_click = 0, 0
            cell_found = False
            for i in range(0, rows):
                for j in range(0, cols):
                    tile_start_pos_x = tile_print_position[(i, j)][0]
                    tile_start_pos_y = tile_print_position[(i, j)][1]
                    if (x_m_click_rel > tile_start_pos_x and x_m_click_rel < tile_start_pos_x + tile_width) and (y_m_click_rel > tile_start_pos_y and y_m_click_rel < tile_start_pos_y + tile_depth):
                        if matrix[i][j] == "":
                            for k in range(tile_count):
                                if game_over == False:
                                    if tiles[k].selected:
                                        if tiles[k].movable:
                                            cell_found = True
                                            dummy = matrix[tiles[k].position_x][tiles[k].position_y]
                                            matrix[tiles[k].position_x][tiles[k].position_y] = matrix[i][j]
                                            matrix[i][j] = dummy
                                            tiles[k].position_x = i
                                            tiles[k].position_y = j
                                            tiles[k].start_pos_x = tile_print_position[(i, j)][0]
                                            tiles[k].start_pos_y = tile_print_position[(i, j)][1]
                                            move_count += 1
                                            isGameOver()
                                            check_mobility()
                    if cell_found == False:
                        for k in range(tile_count):
                            if tiles[k].selected:
                                mat_pos_x = tiles[k].position_x
                                mat_pos_y = tiles[k].position_y
                                tiles[k].start_pos_x = tile_print_position[(mat_pos_x, mat_pos_y)][0]
                                tiles[k].start_pos_y = tile_print_position[(mat_pos_x, mat_pos_y)][1]
                                break
    for i in range(tile_count):
        tiles[i].draw_tyle()
    # Allows only a portion of the screen to update, instead of the entire area, If no argument is passed it updates the entire Surface area like pygame.
    pygame.display.flip()
# Update the whole screen
pygame.display.update()

# Sound effects from zachs23's Ordinary Adventure, Flappy Bird (Original), and Discord
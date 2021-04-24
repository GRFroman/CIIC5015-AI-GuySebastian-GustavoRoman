import pygame

# Windows size
WIDTH, HEIGHT = 800, 800
# Checkers board layout, we are using 8x8
ROWS, COLS = 8, 8
# Board square size
SQUARE_SIZE = WIDTH//COLS
# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

#Piece Values
pygame.font.init()
FONT = pygame.font.Font(pygame.font.get_default_font(), 30)
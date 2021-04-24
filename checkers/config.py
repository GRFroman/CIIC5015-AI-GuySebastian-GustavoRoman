import pygame

# Windows size
WIDTH, HEIGHT = 800, 800
# Checkers board layout, we are using 8x8
ROWS, COLS = 8, 8
# Board square size
SQUARE_SIZE = WIDTH//COLS
# Colors
_RED = (244, 67, 54)
_WHITE = (255, 255, 255)
_BLACK = (33, 33, 33)
_BLUE = (3, 169, 244)
GRAY = (128, 128, 128)

BOARD_COLOR1 = _BLACK
BOARD_COLOR2 = _RED
POSSIBLE_MOVE_COLOR = _BLUE

PLAYER_COLOR_TOP = _WHITE
PLAYER_COLOR_BOTTOM = _RED

#Piece Values
pygame.font.init()
FONT = pygame.font.Font(pygame.font.get_default_font(), 30)
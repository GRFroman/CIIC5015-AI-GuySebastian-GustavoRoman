import pygame
from .config import WHITE, RED, SQUARE_SIZE, GRAY, FONT

class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.direction = 1 if self.color == WHITE else -1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """
        Calculate the position relative to the window board
        """
        getLoc = lambda pos: SQUARE_SIZE * pos + SQUARE_SIZE // 2
        self.x = getLoc(self.col)
        self.y = getLoc(self.row)

    def make_king(self):
        """
        Turn piece into a king
        """
        self.king = True

    def draw(self, window):
        """
        Draw piece
        :param window: Window to be drawn on
        """
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GRAY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            img = FONT.render('K', True, WHITE if self.color == RED else RED)
            window.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))

    def move(self, row, col):
        """
        Update the piece's position
        :param row: Target row
        :param col: Target column
        """
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        """
        The piece's obj representation is its color string
        :return: OBJ rep
        """
        return str(self.color)
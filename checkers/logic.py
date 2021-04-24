import pygame
from .config import PLAYER_COLOR_TOP, PLAYER_COLOR_BOTTOM, POSSIBLE_MOVE_COLOR, SQUARE_SIZE
from .board import Board


class Game:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        """
        Update general game logic
        """
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER_COLOR_BOTTOM
        self.valid_moves = {}

    def winner(self):
        """
        Determine winner if there is one
        :return: Winner or Nonetype
        """
        return self.board.winner()

    def reset(self):
        """
        Reset the board
        """
        self._init()

    def select(self, row, col):
        """
        Select current place, if there is a piece there and its that color's turn then calculate possible moves
        :param row: Target row
        :param col: Target column
        :return: If piece is present
        """
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def _move(self, row, col):
        """
        Internal function to move a piece if allowed
        :param row: Target row
        :param col: Target column
        :return: If move was valid
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        """
        Draws a visual representation of that piece's possible moves
        :param moves: Which moves to highlight
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, POSSIBLE_MOVE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        """
        Cycle turns
        """
        self.valid_moves = {}
        if self.turn == PLAYER_COLOR_BOTTOM:
            self.turn = PLAYER_COLOR_TOP
        else:
            self.turn = PLAYER_COLOR_BOTTOM

    def get_board(self):
        """
        Return the board
        :return: board
        """
        return self.board

    def actor_move(self, board):
        """
        The actor can pass a new board object to update the game
        :param board: New board
        """

        self.board = board
        self.change_turn()
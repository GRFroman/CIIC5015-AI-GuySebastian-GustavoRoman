import pygame
from checkers.config import WIDTH, HEIGHT, PLAYER_COLOR_TOP, PLAYER_COLOR_BOTTOM, SQUARE_SIZE
from checkers.logic import Game
from intelligence_models.minimax import minimax
from intelligence_models.random import random_actor

FPS = 60
minimax_depth = 5
user_play = True

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers AI")

def get_pos_from_mouse(pos):
    """
    Calculate the row and column of the board in relation to the mouse click coordinate
    :param pos: Mouse click coordinates
    :return: relative row and column
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    """
    Main event loop
    """
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        if game.turn == PLAYER_COLOR_TOP:
            value, new_board = minimax(game.get_board(), minimax_depth, True)
            if new_board is None:
                print_winner(PLAYER_COLOR_BOTTOM)
                run = False
            else:
                game.actor_move(new_board)

        elif not user_play:
            if game.turn == PLAYER_COLOR_BOTTOM:
                new_board = random_actor(game.get_board(), game.turn)
                if new_board is None:
                    print_winner(PLAYER_COLOR_TOP)
                    run = False
                else:
                    game.actor_move(new_board)

        if game.winner() is not None:
            print_winner(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

def print_winner(winner):
    if winner == PLAYER_COLOR_BOTTOM:
        print("Bottom player wins")
    else:
        print("Top player wins")
    print(winner)

main()
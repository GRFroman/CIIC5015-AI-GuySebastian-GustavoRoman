import pygame
from checkers.config import WIDTH, HEIGHT, PLAYER_COLOR_TOP, PLAYER_COLOR_BOTTOM, SQUARE_SIZE
from checkers.logic import Game
from intelligence_models.minimax import minimax
from intelligence_models.random import random_actor
from intelligence_models.minimax_alpha_beta import alphabeta

FPS = 60

# Tree depths for minimax and minimax-ab
minimax_depth = 3
minimax_ab_depth = 3

# Global variables for game setup manipulation
user_play = False
random_on = True
minimax_on = False
minimax_ab_on = False

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

        # Minimax checkers game
        if minimax_on:
            if game.turn == PLAYER_COLOR_TOP:
                value, new_board = minimax(game.get_board(), minimax_depth, True)
                if new_board is None:
                    print_winner(PLAYER_COLOR_BOTTOM)
                    run = False
                else:
                    game.actor_move(new_board)

            elif not user_play:
                if game.turn == PLAYER_COLOR_BOTTOM:
                    value, new_board = minimax(game.get_board(), minimax_depth, False)
                    if new_board is None:
                        print_winner(PLAYER_COLOR_TOP)
                        run = False
                    else:
                        game.actor_move(new_board)

        # Random checkers game
        if random_on:
            if game.turn == PLAYER_COLOR_TOP:
                value, new_board = random_actor(game.get_board(), game.turn)
                if new_board is None:
                    print_winner(PLAYER_COLOR_BOTTOM)
                    run = False
                else:
                    game.actor_move(new_board)

            elif not user_play:
                if game.turn == PLAYER_COLOR_BOTTOM:
                    value, new_board = random_actor(game.get_board(), game.turn)
                    if new_board is None:
                        print_winner(PLAYER_COLOR_TOP)
                        run = False
                    else:
                        game.actor_move(new_board)

        # Minimax-ab checkers game
        if minimax_ab_on:
            if game.turn == PLAYER_COLOR_TOP:
                value, new_board = alphabeta(game.get_board(), minimax_ab_depth, float('-inf'), float('inf'), True)
                if new_board is None:
                    print_winner(PLAYER_COLOR_BOTTOM)
                    run = False
                else:
                    game.actor_move(new_board)

            elif not user_play:
                if game.turn == PLAYER_COLOR_BOTTOM:
                    value, new_board = alphabeta(game.get_board(), minimax_ab_depth, float('-inf'), float('inf'), False)
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

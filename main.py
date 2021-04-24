import pygame
from checkers.config import WIDTH, HEIGHT, WHITE, RED, SQUARE_SIZE
from checkers.logic import Game
from minimax.minimax import minimax
FPS = 60
minimax_depth = 3
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

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), minimax_depth, True, game)
            game.actor_move(new_board)

        if not user_play:
            if game.turn == RED:
                value, new_board = minimax(game.get_board(), minimax_depth+1, False, game)
                game.actor_move(new_board)

        if game.winner() != None:
            print(game.winner())
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

main()
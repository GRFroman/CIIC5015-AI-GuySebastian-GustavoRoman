import pygame
from checkers.config import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.logic import Game
FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers AI")

def get_pos_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Event loop
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

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
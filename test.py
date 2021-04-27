import pygame
import time
from checkers.config import WIDTH, HEIGHT, PLAYER_COLOR_TOP, PLAYER_COLOR_BOTTOM, SQUARE_SIZE
from checkers.logic import Game
from intelligence_models.minimax import minimax
from intelligence_models.random import random_actor
from intelligence_models.minimax_alpha_beta import alphabeta

FPS = 60
TIE = (-1, -1, -1)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers Tester")

def use_minimax(board, turn, tree_depth):
    color = True if turn == PLAYER_COLOR_TOP else False
    start_time = time.time()
    _, new_board = minimax(board, tree_depth, color)
    end_time = time.time() - start_time

    return board, end_time

def use_alphabeta(board, turn, tree_depth):
    color = True if turn == PLAYER_COLOR_TOP else False
    start_time = time.time()
    _, new_board = alphabeta(board, tree_depth, float('-inf'), float('inf'), color)
    end_time = time.time() - start_time

    return board, end_time

class Random:
    def __init__(self):
        self.name = "Random"

    def getName(self):
        return self.name

    def run(self, board, turn):
        start_time = time.time()
        _, new_board = random_actor(board, turn)
        end_time = time.time() - start_time

        return new_board, end_time

class Minimax:
    def __init__(self, depth):
        self.tree_depth = depth
        self.name = f"Minimax {depth}"

    def getName(self):
        return self.name

    def run(self, board, turn):
        color = True if turn == PLAYER_COLOR_TOP else False
        start_time = time.time()
        _, new_board = minimax(board, self.tree_depth, color)
        end_time = time.time() - start_time

        return new_board, end_time

class AlphaBeta:
    def __init__(self, depth):
        self.tree_depth = depth
        self.name = f"AlphaBeta {depth}"

    def getName(self):
        return self.name

    def run(self, board, turn):
        color = True if turn == PLAYER_COLOR_TOP else False
        start_time = time.time()
        _, new_board = alphabeta(board, self.tree_depth, float('-inf'), float('inf'), color)
        end_time = time.time() - start_time

        return new_board, end_time

# Schedule of competitions
parings = [
    (Random(), Minimax(1)),
    (Random(), AlphaBeta(1)),
    (Random(), Minimax(2)),
    (Random(), AlphaBeta(2)),
    (Random(), Minimax(3)),
    (Random(), AlphaBeta(3)),
    (Random(), Minimax(4)),
    (Random(), AlphaBeta(4)),
]

# Generate the minimax v alphabeta matches
for i in range(1, 5):
    for j in range(1, 5):
        parings.append((Minimax(i), AlphaBeta(j)))

parings.append((Minimax(i), AlphaBeta(j)))

final_scores = {}

with open("results.txt", 'w') as output:
    for pair in parings:
        # Add items to final scores
        for p in pair:
            if p.getName() not in final_scores:
                final_scores[p.getName()] = [[0, 0], [0, 0], [0, 0]]


        print(f"{pair[0].getName()} vs. {pair[1].getName()}")
        # Reinitialize the program
        run = True
        clock = pygame.time.Clock()
        game = Game(WINDOW)

        # Time Metrics
        player_total = [0, 0]
        player_count = [0, 0]
        player_max = [float('-inf'), float('-inf')]
        player_min = [float('inf'), float('inf')]

        winner_color = (0,0,0)

        #Game loop
        while run:
            clock.tick(FPS)

            turn_index = 0 if game.turn == PLAYER_COLOR_TOP else 1

            updated_board, move_time = pair[turn_index].run(game.get_board(), game.turn)

            if updated_board is None:
                winner_color = game.winner()
                run = False
            else:
                game.actor_move(updated_board)

                player_total[turn_index] += move_time
                player_count[turn_index] += 1

                player_min[turn_index] = min(player_min[turn_index], move_time)
                player_max[turn_index] = max(player_max[turn_index], move_time)

            if game.winner() is not None:
                winner_color = game.winner()
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        run = False
                        winner_color = (-1, -1, -1)


            game.update()

        scores = final_scores[pair[0].getName()]
        scores[0][0] += player_total[0]/player_count[0]
        scores[0][1] += 1
        scores[1][0] += player_max[0]
        scores[1][1] += 1
        scores[2][0] += player_min[0]
        scores[2][1] += 1
        final_scores[pair[0].getName()] = scores

        scores = final_scores[pair[1].getName()]
        scores[0][0] += player_total[1] / player_count[1]
        scores[0][1] += 1
        scores[1][0] += player_max[1]
        scores[1][1] += 1
        scores[2][0] += player_min[1]
        scores[2][1] += 1
        final_scores[pair[1].getName()] = scores

        winner = "Tie because of loop" if winner_color == TIE else pair[0].getName() if winner_color == PLAYER_COLOR_TOP else pair[1].getName()
        output.write(f"{pair[0].getName()} vs. {pair[1].getName()} : Winner: {winner}\n")
        output.write("{:10} {:10} {:10} {:10}\n".format("Model Name", "Average", "Maximum", "Minimum"))
        output.write("{:10} {:10} {:10} {:10}\n".format(pair[0].getName(), player_total[0]/player_count[0], player_max[0], player_min[0]))
        output.write("{:10} {:10} {:10} {:10}\n\n".format(pair[1].getName(), player_total[1]/player_count[1], player_max[1], player_min[1]))

        print(f"{pair[0].getName()} vs. {pair[1].getName()} : Winner: {winner}\n")
        print("{:10} {:10} {:10} {:10}\n".format("Model Name", "Average", "Maximum", "Minimum"))
        print("{:10} {:10} {:10} {:10}\n".format(pair[0].getName(), player_total[0] / player_count[0], player_max[0],player_min[0]))
        print("{:10} {:10} {:10} {:10}\n\n".format(pair[1].getName(), player_total[1] / player_count[1], player_max[1],player_min[1]))

    for names, scores in final_scores.items():
        output.write(f"{names} {scores[0][0]/scores[0][1]} {scores[1][0]/scores[1][1]} {scores[2][0]/scores[2][1]}\n")
    pygame.quit()

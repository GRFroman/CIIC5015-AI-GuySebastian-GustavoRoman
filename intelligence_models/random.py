import random

from .ai_utils import get_all_moves


def random_actor(board, player):
    """
    A random actor that picks an available move at random
    :param board: The board obj
    :param player: The player that the AI represents
    :return: A board
    """

    # Obtain all possible moves from the current board
    moves = get_all_moves(board, player)

    # Verify there are possible moves to choose from
    if len(moves) == 0:
        return 0, None

    # Return a random move from the randomized sample
    return 0, moves[random.randint(0, len(moves)-1)]

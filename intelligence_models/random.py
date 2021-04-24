import random

from .ai_utils import get_all_moves


def random_actor(board, player):
    """
    A random actor that picks an available move at random
    :param board: The board obj
    :param player: The player that the AI represents
    :return: A board
    """

    # First the AI gets all the possible moves
    moves = get_all_moves(board, player)
    if len(moves) == 0:
        return None
    return moves[random.randint(0, len(moves)-1)]

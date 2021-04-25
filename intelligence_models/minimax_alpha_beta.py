from copy import deepcopy

from .ai_utils import get_all_moves

PLAYER_COLOR_BOTTOM = (244, 67, 54)
PLAYER_COLOR_TOP = (255, 255, 255)


def alphabeta(position, depth, a, b, max_player):
    """
    Recursive function to determine best possible move
    :param position: Current pos actor is currently in
    :param depth: Tree depth
    :param a: minimum score for maxing player
    :param b: maximum score for minimizing player
    :param max_player: Color which whe are working with
    :return: Board
    """

    # Break recursion if done or the game is over
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        # Anything is better that the current path
        max_value = float('-inf')

        best_move = None

        for move in get_all_moves(position, PLAYER_COLOR_TOP):
            value = alphabeta(move, depth - 1, a, b, False)[0]
            max_value = max(max_value, value)
            a = max(a, max_value)
            if a >= b:
                break
            best_move = move if max_value == value else best_move

        return max_value, best_move

    else:
        # Anything is better that the current path
        min_value = float('inf')

        best_move = None

        for move in get_all_moves(position, PLAYER_COLOR_BOTTOM):
            value = alphabeta(move, depth - 1, a, b, True)[0]
            min_value = min(min_value, value)
            b = min(b, min_value)
            if a >= b:
                break

            best_move = move if min_value == value else best_move

        return min_value, best_move

from copy import deepcopy

from .ai_utils import get_all_moves

PLAYER_COLOR_BOTTOM = (244, 67, 54)
PLAYER_COLOR_TOP = (255, 255, 255)


def minimax(position, depth, max_player):
    """
    Recursive function to determine best possible move
    :param position: Current pos actor is currently in
    :param depth: Tree depth
    :param max_player: Color which whe are working with
    :return: Board
    """

    # Break recursion if done or the game is over
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        # Anything is better that the current path
        maxEval = float('-inf')

        best_move = None

        for move in get_all_moves(position, PLAYER_COLOR_TOP):
            evaluation = minimax(move, depth - 1, False)[0]
            maxEval = max(maxEval, evaluation)
            best_move = move if maxEval == evaluation else best_move

        return maxEval, best_move

    else:
        # Anything is better that the current path
        minEval = float('+inf')

        best_move = None

        for move in get_all_moves(position, PLAYER_COLOR_BOTTOM):
            evaluation = minimax(move, depth - 1, True)[0]
            minEval = min(minEval, evaluation)
            best_move = move if minEval == evaluation else best_move

        return minEval, best_move

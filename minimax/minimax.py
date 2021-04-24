from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position, depth, max_player, game):
    """
    Recursive function to determine best possible move
    :param position: Current pos actor is currently in
    :param depth: Tree depth
    :param max_player: Color which whe are working with
    :param game: The game logic object
    :return:
    """

    # Break recursion if done or the game is over
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        # Anything is better that the current path
        maxEval = float('-inf')

        best_move = None

        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            best_move = move if maxEval == evaluation else best_move

        return maxEval, best_move

    else:
        # Anything is better that the current path
        minEval = float('+inf')

        best_move = None

        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            best_move = move if minEval == evaluation else best_move

        return minEval, best_move


def get_all_moves(board, color, game):
    """
    Gets all the possible moves for that color in that board
    :param board: Board to iterate over
    :param color: Piece color
    :param game: Game logic
    :return: All possible moves
    """
    # Array of possible board layouts
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # Fix, deep copy avoids using the existing list object
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, board, game, skip):
    """
    Simulates a board movement
    :param piece: Piece to be moved
    :param move: Where to move the piece
    :param board: Where the piece will be moved
    :param game: The game logic
    :param skip: Determines if move is a piece skip or just a move
    :return: Edited board
    """

    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board
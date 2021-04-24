from copy import deepcopy


def get_all_moves(board, color):
    """
    Gets all the possible moves for that color in that board
    :param board: Board to iterate over
    :param color: Piece color
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
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, board, skip):
    """
    Simulates a board movement
    :param piece: Piece to be moved
    :param move: Where to move the piece
    :param board: Where the piece will be moved
    :param skip: Determines if move is a piece skip or just a move
    :return: Edited board
    """

    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

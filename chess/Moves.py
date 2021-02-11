from typing import List

from chess import Board
from chess.Box import Box


def is_a_box(i: int, j: int) -> bool:
    return (0 <= i < 8) and (0 <= j < 8)


def is_capturable(board: List[List[Box]], i1, j1, i2, j2) -> bool:
    box_1 = board[i1][j1]
    box_2 = board[i2][j2]
    if not box_2.is_occupied():
        return True
    else:
        piece_1 = box_1.get_piece()
        piece_2 = box_2.get_piece()
        if piece_1 and piece_1.color != piece_2.color:
            print(piece_1.color, piece_2.color)
            return True
    return False


def get_pawn_moves(board: List[List[Box]], i: int, j: int) -> List[List[int]]:
    list_of_moves = []
    box = board[i][j]
    piece = box.get_piece()
    if piece and piece.piece_type == 'Pawn':
        pass
    return list_of_moves


def get_rook_moves(board: List[List[Box]], i: int, j: int) -> List[List[int]]:
    list_of_moves = []
    box = board[i][j]
    piece = box.get_piece()
    if piece and piece.piece_type == 'Rook':
        pass
    return list_of_moves


def get_knight_moves(board: List[List[Box]], i: int, j: int) -> List[List[int]]:
    list_of_moves = []
    box = board[i][j]
    piece = box.get_piece()
    if piece and piece.piece_type == 'Knight':
        pass
    return list_of_moves


def get_bishop_moves(board: List[List[Box]], i: int, j: int) -> List[List[int]]:
    list_of_moves = []
    box = board[i][j]
    piece = box.get_piece()
    if piece and piece.piece_type == 'Bishop':
        pass
    return list_of_moves


def get_queen_moves(board: List[List[Box]], i: int, j: int) -> List[List[int]]:
    list_of_moves = []
    box = board[i][j]
    piece = box.get_piece()
    if piece and piece.piece_type == 'Queen':
        pass
    return list_of_moves


def get_king_moves(board: List[List[Box]], i: int, j: int) -> List[List[int]]:
    # TODO: Test it
    list_of_moves = []
    available_locations = [[i + x, j + y] for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]
    available_locations = [elem for elem in available_locations if is_a_box(elem[0], elem[1])]
    print(available_locations)
    for location in available_locations:
        if is_capturable(board, i, j, location[0], location[1]):
            list_of_moves.append([[i, j], location])

    return list_of_moves


def get_available_moves(board: List[List[Box]], i: int, j: int) -> List:
    list_of_moves = []
    box = board[i][j]
    if box.is_occupied():
        piece = box.get_piece()

        if piece.piece_type == 'Pawn':
            list_of_moves = get_pawn_moves(board, i, j)

        if piece.piece_type == 'Rook':
            list_of_moves = get_rook_moves(board, i, j)

        if piece.piece_type == 'Knight':
            list_of_moves = get_knight_moves(board, i, j)

        if piece.piece_type == 'Bishop':
            list_of_moves = get_bishop_moves(board, i, j)

        if piece.piece_type == 'Queen':
            list_of_moves = get_queen_moves(board, i, j)

        if piece.piece_type == 'King':
            list_of_moves = get_king_moves(board, i, j)

    return list_of_moves


"""The Added move shouldn't result in own check"""


def get_all_available_moves(board: List[List[Box]]):
    """

    :type board: List[List[Box]]
    """
    list_of_moves = []
    for i in range(8):
        for j in range(8):
            moves = get_available_moves(board, i, j)
            if moves:
                list_of_moves.extend(moves)
    return list_of_moves

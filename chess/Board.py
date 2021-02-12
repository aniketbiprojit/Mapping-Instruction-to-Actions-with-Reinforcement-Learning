from chess.Box import Box
from typing import List

from chess.Moves import get_all_available_moves
from chess.Piece import Piece

board: List[List[Box]] = [[Box(i, j) for j in range(8)] for i in range(8)]

pieces_names = {
    'King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn'
}


def init_board(board_: List[List[Box]]) -> List[List[Box]]:
    """

    :type board_: List[List[Box]]
    """
    for j in range(8):
        board_[1][j].set_piece(Piece('Black', 'Pawn'))

    for j in range(8):
        board_[6][j].set_piece(Piece('White', 'Pawn'))

    board_[0][0].set_piece((Piece('Black', 'Rook')))
    board_[0][1].set_piece((Piece('Black', 'Knight')))
    board_[0][2].set_piece((Piece('Black', 'Bishop')))
    board_[0][3].set_piece((Piece('Black', 'Queen')))
    board_[0][4].set_piece((Piece('Black', 'King')))
    board_[0][5].set_piece((Piece('Black', 'Bishop')))
    board_[0][6].set_piece((Piece('Black', 'Knight')))
    board_[0][7].set_piece((Piece('Black', 'Rook')))

    board_[3][3].set_piece((Piece('White', 'Queen')))

    board_[7][0].set_piece((Piece('White', 'Rook')))
    board_[7][1].set_piece((Piece('White', 'Knight')))
    board_[7][2].set_piece((Piece('White', 'Bishop')))
    board_[7][3].set_piece((Piece('White', 'Queen')))
    board_[7][4].set_piece((Piece('White', 'King')))
    board_[7][5].set_piece((Piece('White', 'Bishop')))
    board_[7][6].set_piece((Piece('White', 'Knight')))
    board_[7][7].set_piece((Piece('White', 'Rook')))

    return board_


def convert_box_to_dict(board_: List[List[Box]]):
    outer_list = []
    for i in range(8):
        inner_list = []
        for j in range(8):
            box = board_[i][j]
            export_dict = {"i": i, "j": j, "occupied": box.is_occupied(),
                           "piece_type": box.get_piece() and box.get_piece().piece_type,
                           "color": box.get_piece() and box.get_piece().color}
            inner_list.append(export_dict)
        outer_list.append(inner_list)

    # print(outer_list)
    return outer_list


def convert_dict_to_box(export_dict):
    board_: List[List[Box]] = [[Box(i, j) for j in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            elem = export_dict[i][j]
            if elem["occupied"]:
                board_[i][j].set_piece(Piece(elem['color'], elem['piece_type']))

    return board_


def update_board(board:List[List[Box]], move_from, move_to):
    if [move_from, move_to] in get_all_available_moves(board):
        first_position = board[move_from[0]][move_from[1]]
        second_position = board[move_to[0]][move_to[1]]
        if second_position.is_occupied():
            second_position.remove_piece()
        second_position.set_piece(first_position.get_piece())
        first_position.remove_piece()
    return board
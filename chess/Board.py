from chess.Box import Box
from typing import List

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

    # board_[3][3].set_piece((Piece('White', 'Rook')))

    board_[7][0].set_piece((Piece('White', 'Rook')))
    board_[7][1].set_piece((Piece('White', 'Knight')))
    board_[7][2].set_piece((Piece('White', 'Bishop')))
    board_[7][3].set_piece((Piece('White', 'Queen')))
    board_[7][4].set_piece((Piece('White', 'King')))
    board_[7][5].set_piece((Piece('White', 'Bishop')))
    board_[7][6].set_piece((Piece('White', 'Knight')))
    board_[7][7].set_piece((Piece('White', 'Rook')))

    return board_

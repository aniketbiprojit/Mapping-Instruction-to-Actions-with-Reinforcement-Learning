from chess.Box import Box
from typing import List

board: List[List[Box]] = [[Box(i, j) for j in range(8)] for i in range(8)]

pieces_names = {
    'King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn'
}


def init_board(board_: List[List[Box]]) -> List[List[Box]]:
    """

    :type board_: List[List[Box]]
    """

    return board_

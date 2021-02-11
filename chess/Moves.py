from typing import List

from chess import Board
from chess.Box import Box


def get_available_moves(board: List[List[Box]], i: int, j: int) -> List:
    list_of_moves = []
    if board[i][j].is_occupied():
        pass
    return list_of_moves


def get_all_available_moves(board: Board.board):
    list_of_moves = []
    for i in range(8):
        for j in range(8):
            moves = get_available_moves(board, i, j)
            if moves:
                list_of_moves.extend(moves)
    return list_of_moves

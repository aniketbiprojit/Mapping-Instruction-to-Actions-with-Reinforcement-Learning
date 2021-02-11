from typing import List

from chess import Board
from chess.Box import Box


def get_pawn_moves() -> List[List[int]]:
    list_of_moves = []
    return list_of_moves


def get_rook_moves() -> List[List[int]]:
    list_of_moves = []
    return list_of_moves


def get_knight_moves() -> List[List[int]]:
    list_of_moves = []
    return list_of_moves


def get_bishop_moves() -> List[List[int]]:
    list_of_moves = []
    return list_of_moves


def get_queen_moves() -> List[List[int]]:
    list_of_moves = []
    return list_of_moves


def get_king_moves() -> List[List[int]]:
    list_of_moves = []
    return list_of_moves


def get_available_moves(board: List[List[Box]], i: int, j: int) -> List:
    list_of_moves = []
    box = board[i][j]
    if box.is_occupied():
        piece = box.get_piece()

        if piece.piece_type == 'Pawn':
            list_of_moves = get_pawn_moves()

        if piece.piece_type == 'Rook':
            list_of_moves = get_rook_moves()

        if piece.piece_type == 'Knight':
            list_of_moves = get_knight_moves()

        if piece.piece_type == 'Bishop':
            list_of_moves = get_bishop_moves()

        if piece.piece_type == 'Queen':
            list_of_moves = get_queen_moves()

        if piece.piece_type == 'King':
            list_of_moves = get_king_moves()

    return list_of_moves


def get_all_available_moves(board: Board.board):
    list_of_moves = []
    for i in range(8):
        for j in range(8):
            moves = get_available_moves(board, i, j)
            if moves:
                list_of_moves.extend(moves)
    return list_of_moves

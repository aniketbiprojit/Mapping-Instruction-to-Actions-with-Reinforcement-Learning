from typing import List

from chess import Board
from chess.Box import Box


def is_a_box(i, j):
    return (0 <= i < 8) and (0 <= j < 8)


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
    list_of_moves = []
    box = board[i][j]
    piece = box.get_piece()
    if piece and piece.piece_type == 'King':
        pass
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


def get_all_available_moves(board: Board.board):
    list_of_moves = []
    for i in range(8):
        for j in range(8):
            moves = get_available_moves(board, i, j)
            if moves:
                list_of_moves.extend(moves)
    return list_of_moves

""""""
from typing import List

# noinspection SpellCheckingInspection
from chess.Box import Box
from chess.Moves import get_all_available_moves

alphabets = 'abcdefgh'.upper()


def get_chess_alpha_numeric(i, j):
    return f"{alphabets[i]}{8 - j}"


def get_base_statement(move_from, move_to):
    return f"Move from position {get_chess_alpha_numeric(move_from[0], move_from[1])} to {get_chess_alpha_numeric(move_to[0], move_to[1])}"


def get_piece_statement(board: List[List[Box]], move_from: List[int], move_to: List[int]):
    return f"Move {board[move_from[0]][move_from[1]].get_piece().piece_type} to {get_chess_alpha_numeric(move_to[0], move_to[1])}"


def generate_textual_data(board: List[List[Box]], move_from: List[int], move_to: List[int]):
    data = [(get_base_statement(move_from, move_to)), get_piece_statement(board, move_from, move_to)]
    return data


def generate_input_output(board: List[List[Box]]):
    all_possible_statements = []
    for moves in get_all_available_moves(board):
        # noinspection PyDictCreation
        inner_dict = {}

        # Input
        inner_dict['statements'] = (generate_textual_data(board, moves[0], moves[1]))
        inner_dict['turn_of'] = board[moves[0][0]][moves[0][1]].get_piece().color

        # Output
        inner_dict['move_from'] = moves[0]
        inner_dict['move_to'] = moves[1]
        all_possible_statements.append(inner_dict)
    return all_possible_statements

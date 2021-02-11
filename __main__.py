"""___main__.py"""
from json import loads

from chess import Board
from chess.Board import convert_box_to_dict, convert_dict_to_box
from chess.Moves import get_all_available_moves
from textual.Generate import generate_textual_data

if __name__ == '__main__':
    board = Board.init_board(Board.board)
    for i in range(8):
        print(board[i])

    # convert_dict_to_box(json.loads(export_dict))
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

    print(all_possible_statements)

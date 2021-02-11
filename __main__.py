"""___main__.py"""
from chess import Board
from chess.Board import convert_box_to_dict
from chess.Moves import get_all_available_moves

if __name__ == '__main__':
    board = Board.init_board(Board.board)
    for i in range(8):
        print(board[i])

    convert_box_to_dict(board)
    # for moves in get_all_available_moves(board):
    #     print(moves, board[moves[0][0]][moves[0][1]])
    #     pass

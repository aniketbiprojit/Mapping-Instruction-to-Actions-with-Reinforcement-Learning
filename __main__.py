"""___main__.py"""
from json import loads

from chess import Board
from chess.Board import update_board
from chess.Moves import get_all_available_moves

if __name__ == '__main__':
    import training.model
    # board = Board.init_board(Board.board)
    # for i in range(8):
    #     print(board[i])
    #
    # print()
    #
    # board = update_board(board, [0, 1], [2, 2])
    # for i in range(8):
    #     print(board[i])


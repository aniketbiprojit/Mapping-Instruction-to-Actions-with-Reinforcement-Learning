"""___main__.py"""
from chess import Board
from chess.Moves import get_all_available_moves

if __name__ == '__main__':
    board = Board.init_board(Board.board)
    for i in range(8):
        print(board[i])

    print(get_all_available_moves(board))

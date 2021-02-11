"""___main__.py"""
from chess import Board
from chess.Moves import get_all_available_moves

if __name__ == '__main__':
    board = Board.init_board(Board.board)
    for i in range(8):
        print(board[i])

    for moves in get_all_available_moves(board):
        print(moves, board[moves[0][0]][moves[0][1]])
        pass

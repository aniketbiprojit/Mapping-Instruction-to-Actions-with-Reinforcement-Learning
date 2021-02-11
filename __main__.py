"""___main__.py"""
from chess import Board

if __name__ == '__main__':
    for i in range(8):
        for j in range(8):
            print(Board.board[i][j], end=', ')
        print()

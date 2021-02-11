"""___main__.py"""
from json import loads

from chess import Board

if __name__ == '__main__':
    board = Board.init_board(Board.board)
    for i in range(8):
        print(board[i])

    # convert_dict_to_box(json.loads(export_dict))
    

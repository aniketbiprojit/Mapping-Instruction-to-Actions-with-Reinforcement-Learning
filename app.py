from random import randint
from typing import List

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from chess.Board import init_board, convert_box_to_dict, convert_dict_to_box, update_board
from chess.Box import Box
from chess.Moves import get_all_available_moves

import json

# from flask_cors import CORS

app = Flask(__name__, static_folder='./static', template_folder='./template')
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# noinspection SpellCheckingInspection
socketio: SocketIO = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template("index.html")


@socketio.on('get available moves')
def available_moves(data):
    board_dict = json.loads(str(data))
    board = convert_dict_to_box(board_dict)

    moves = get_all_available_moves(board)
    emit('available moves', moves)


@socketio.on('get_update')
def update_board_socket(data):
    board_dict = json.loads(str(data))
    board = convert_dict_to_box(board_dict)

    moves = get_all_available_moves(board)
    move = moves[randint(0, len(moves) - 1)]
    # for ?move in (moves):

    board = update_board(board, move[0], move[1])
    board = convert_box_to_dict(board)

    emit('update_board', json.dumps(board))
    # for i in range(8):
    #     print(board[i])


@socketio.on('connected')
def handle_my_custom_event(json_):
    # print('received json: ' + str(json_))
    board = [[Box(i, j) for j in range(8)] for i in range(8)]
    board = init_board(board)
    board = convert_box_to_dict(board)
    # print(board)
    emit('init', json.dumps(board))


if __name__ == '__main__':
    socketio.run(app)

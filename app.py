from typing import List

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from chess.Board import init_board
from chess.Box import Box
from chess.Moves import get_all_available_moves

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
    print('received data: ' + str(data))
    # TODO: CONVERT data to python readable format.
    moves = get_all_available_moves(data)
    emit('available moves', moves)


@socketio.on('connected')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    board: List[List[Box]] = [[Box(i, j) for j in range(8)] for i in range(8)]
    board = init_board(board)
    # TODO: Board Conversion
    emit('init', board)


if __name__ == '__main__':
    socketio.run(app)

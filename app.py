from flask import Flask, render_template
from flask_socketio import SocketIO

# from flask_cors import CORS

app = Flask(__name__, static_folder='./static', template_folder='./template')
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# noinspection SpellCheckingInspection
socketio: SocketIO = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template("index.html")


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    socketio.run(app)

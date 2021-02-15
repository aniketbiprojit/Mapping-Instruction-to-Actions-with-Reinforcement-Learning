from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import tensorflow as tf

from chess.Board import init_board, board, update_board
from data.generate_inputs import get_values_input

import numpy as np

board = init_board(board)


def get_input_data(board_):
    board_input, text_input, move_output = get_values_input(board_)

    text_input = np.asarray(text_input)
    board_input = [np.append(i, 0) for i in board_input]
    board_input.append(text_input)
    board_input = np.asarray(board_input)
    return board_input, np.asarray([move_output])


input_data, output_data = get_input_data(board)

inp = Input((1 * 6))
x = Dense(8)(inp)
x = Dense(32)(x)
x = Dense(32)(x)
x = Dense(8)(x)
output = Dense(2, activation='sigmoid')(x)

model = Model(inp, output)
model.compile()

print(model.summary())

loss_data = []


def loss_function(y, logits):
    y *= 64
    logits *= 64
    i_1, j_1 = (logits[0][0] // 8, logits[0][0] % 8)
    i_2, j_2 = (y[0][0] // 8, y[0][0] % 8)
    loss_data.append([[i_1.numpy(), j_1.numpy()], [i_2.numpy(), j_2.numpy()]])
    return (i_1 - i_2) ** 2 + (j_1 - j_2) ** 2


optimizer = tf.keras.optimizers.SGD(learning_rate=1e-3)

# print(o)
for _ in range(100):
    input_data, output_data = get_input_data(board)
    for i in range(100):
        with tf.GradientTape() as tape:
            # for i in range(100):
            state = tf.convert_to_tensor(input_data[64].reshape(6), dtype='float32')
            state = tf.expand_dims(state, 0)
            loss = loss_function(model(state), tf.convert_to_tensor(output_data, dtype='float32'))
            print(loss)
        grads = tape.gradient(loss, model.trainable_weights)
        optimizer.apply_gradients(zip(grads, model.trainable_weights))

        board = update_board(board, [int(output_data[0][0] * 64 // 8), int(output_data[0][0] * 64 % 8)],
                             [int(output_data[0][1] * 64 // 8), int(output_data[0][1] * 64 % 8)])

        print(loss)
print(loss_data)
# break
# input_data, output_data = get_input_data(board)

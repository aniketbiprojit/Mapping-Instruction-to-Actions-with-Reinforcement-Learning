from typing import List

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import tensorflow as tf

from chess.Board import init_board, board, update_board
from chess.Box import Box
from chess.Moves import get_all_available_moves
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

print(input_data, output_data)
# inp = Input((1 * 6))
# x = Dense(8)(inp)
# x = Dense(32)(x)
# x = Dense(32)(x)
# x = Dense(8)(x)
# output = Dense(2, activation='softmax')(x)
#
# model = Model(inp, output)
# model.compile()
#
# print(model.summary())

loss_data = []


def euclid(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def value_function(selected_move, move_original):
    return euclid(selected_move[0], move_original[0]) + euclid(selected_move[1], move_original[1])


class Environment:

    def reset(self):
        self.board = init_board(self.board)
        return self.board

    def update(self, move_from, move_to):
        self.board = update_board(self.board, move_from, move_to)
        return self.board

    def __init__(self, board_: List[List[Box]] = []):
        if not board_:
            self.board = init_board([[Box(i, j) for j in range(8)] for i in range(8)])
        self.actions = get_values_input(self.board)

    def get_actions(self):
        self.actions = get_all_available_moves(self.board)
        return self.actions


# Multi-class actions.
# Change on every update.
# Updating the probability distribution
print(Environment().get_actions())
# def loss_function(y, logits):
#     y *= 64
#     logits *= 64
#     i_1, j_1 = (logits[0][0] // 8, logits[0][0] % 8)
#     i_2, j_2 = (y[0][0] // 8, y[0][0] % 8)
#     loss_data.append([[i_1.numpy(), j_1.numpy()], [i_2.numpy(), j_2.numpy()]])
#     return (i_1 - i_2) ** 2 + (j_1 - j_2) ** 2
#
#
# optimizer = tf.keras.optimizers.SGD(learning_rate=1e-3)
# train_acc_metric = tf.keras.metrics.SparseCategoricalAccuracy()
# # print(o)
# for _ in range(10):
#     board = init_board(board)
#     input_data, output_data = get_input_data(board)
#     for i in range(100):
#         with tf.GradientTape() as tape:
#             # for i in range(100):
#             state = tf.convert_to_tensor(input_data[64].reshape(6), dtype='float32')
#             state = tf.expand_dims(state, 0)
#             loss = loss_function(model(state), tf.convert_to_tensor(output_data, dtype='float32'))
#             # print(loss)
#         grads = tape.gradient(loss, model.trainable_weights)
#         optimizer.apply_gradients(zip(grads, model.trainable_weights))
#
#         # train_acc_metric.update_state(model(state), tf.convert_to_tensor(output_data, dtype='float32'))
#
#         board = update_board(board, [int(output_data[0][0] * 64 // 8), int(output_data[0][0] * 64 % 8)],
#                              [int(output_data[0][1] * 64 // 8), int(output_data[0][1] * 64 % 8)])
#         input_data, output_data = get_input_data(board)
#
#         if i % 80 == 0:
#             print(loss)
#
#     # train_acc = train_acc_metric.result()
#     # print(train_acc)
#     # train_acc_metric.reset_states()
#
# print(loss_data)
# # break
# # input_data, output_data = get_input_data(board)

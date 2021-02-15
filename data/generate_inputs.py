from random import randint
from typing import List

from chess.Box import Box
from data.generate_moves import generate_input_output, vocab
from sklearn.preprocessing import OrdinalEncoder
from chess.Board import board, init_board

import pandas as pd

board = init_board(board)

ord_enc = OrdinalEncoder()

vocab = [i.lower() for i in (list(set(vocab)))]
vocab = {vocab[k]: k for k in range(len(vocab))}


# for i in range(8):
#     print(board[i])


def generate_pandas_row(box: Box):
    data = {'i': box.i, 'j': box.j, }
    colors = {'Black': 0.5, 'White': 1}
    if box.is_occupied():
        data['color'] = box.get_piece().color
        data['piece_type'] = box.get_piece().piece_type
    else:
        data['color'] = 'Empty'
        data['piece_type'] = 'Empty'
    return data


def generate_pandas_df(board_: List[List[Box]]):
    rows = []
    for i in range(8):
        for j in range(8):
            rows.append(generate_pandas_row(board_[i][j]))
    df_ = pd.DataFrame(rows)
    df_ = pd.get_dummies(df_, columns=['color'])
    df_['index'] = (df_['i'] * 8 + df_['j']) / 64
    return df_


def ordinal_encoding(df_):
    df_['piece_type_code'] = (ord_enc.fit_transform(df_[['piece_type']])) / 6
    return df_


def inverse_transform(df_):
    df_['piece_type'] = ord_enc.inverse_transform(df_[['piece_type_code']] * 6)
    return df_


def get_values_input(board_):
    df_ = generate_pandas_df(board_)
    df_ = ordinal_encoding(df_)

    moves = generate_input_output(board)

    move = moves[randint(0, len(moves) - 1)]

    move_input = move['statements'][0].split(' ')
    move_input = [vocab[i.lower()] for i in move_input]

    output_data = [(move['move_from'][0] * 8 + move['move_from'][1]) / 64,
                   (move['move_to'][0] * 8 + move['move_to'][1]) / 64]

    return df_.reset_index(drop=True).drop(['piece_type', 'i', 'j'], axis=1).values, move_input, output_data



# print(vocab)

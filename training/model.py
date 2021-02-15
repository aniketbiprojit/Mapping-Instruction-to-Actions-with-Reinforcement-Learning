from typing import List

from chess.Box import Box
from textual.Generate import get_all_available_moves
from sklearn.preprocessing import OrdinalEncoder
from chess.Board import board, init_board

import pandas as pd

board = init_board(board)


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
    print(df_.head())
    return df_


# print(generate_numerical_data(board[0][0]))
df = generate_pandas_df(board)
df = pd.get_dummies(df, columns=['color', 'piece_type'])
# ord_enc = OrdinalEncoder()

# df['piece_type_code'] = (ord_enc.fit_transform(df[['piece_type']])) / 6
print(df.head())
# print(df.reset_index(drop=True).drop(['piece_type'], axis=1).values)

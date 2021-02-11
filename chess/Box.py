from chess.Piece import Piece


class Box:
    i: int = 0
    j: int = 0
    occupied: bool = False
    piece: Piece

    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

    def get_piece(self):
        if self.occupied:
            return self.piece
        return self.piece

    def set_piece(self):
        pass

    def __repr__(self):
        return f'[{self.i}][{self.j}]'

    def __str__(self):
        return f'[{self.i}][{self.j}]'

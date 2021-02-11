from chess.Piece import Piece


class Box:
    i: int = 0
    j: int = 0
    __occupied: bool = False
    __piece: Piece

    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

    def get_piece(self):
        if self.occupied:
            return self.piece
        return self.piece

    def set_piece(self, piece: Piece):
        if self.occupied:
            return False
        self.occupied = True
        self.piece = piece
        return True

    def remove_piece(self):
        if self.occupied:
            return True
        self.piece = None
        return True

    def is_occupied(self):
        return self.occupied

    def __repr__(self):
        return f'[{self.i}][{self.j}]'

    def __str__(self):
        return f'[{self.i}][{self.j}]'

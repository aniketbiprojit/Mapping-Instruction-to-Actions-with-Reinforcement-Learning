from chess.Piece import Piece


class Box:
    i: int = 0
    j: int = 0
    __occupied: bool = False
    __piece: Piece = None

    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

    def get_piece(self) -> Piece:
        if self.__occupied:
            return self.__piece
        return None

    def set_piece(self, piece: Piece) -> bool:
        if self.__occupied:
            return False
        self.__occupied = True
        self.__piece = piece
        return True

    def remove_piece(self):
        if not self.__occupied:
            return True
        self.__occupied = False
        self.__piece = None
        return True

    def is_occupied(self):
        return self.__occupied

    def __repr__(self):
        if self.__occupied:
            return f'{self.__piece.color[0].lower()}{self.__piece.piece_type[0]} ({self.i},{self.j})'
        else:
            return f'   ({self.i},{self.j})'

    def __str__(self):
        return self.__repr__()

class Piece:
    color: str
    piece_type: str

    def __init__(self, color: str, piece_type: str) -> None:
        self.color = color
        self.piece_type = piece_type

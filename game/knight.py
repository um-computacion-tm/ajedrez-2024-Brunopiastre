from game.piece import Piece

class Knight(Piece):
    def __str__(self):
        if self.color == "WHITE":
            return "♘"
        else:
            return "♞"
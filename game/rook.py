from game.piece import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"


    def movimientos_validos(self, board):
        movimientos = []
        x, y = self.position
    
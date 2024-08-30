class Piece:
    def __init__(self, color):
        self.color = color

    def movimientos_validos(self, board):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def movimientos_validos(self, board):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

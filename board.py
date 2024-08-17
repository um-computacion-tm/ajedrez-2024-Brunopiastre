from rook import Rook
from pawn import Pawn


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []

            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")
        
        # Colocar los peones negros
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
        
        # Colocar los peones blancos
        for i in range(8):
            self.__positions__[6][i] = Pawn("WHITE")
            

    def get_piece(self, row, col):
        return self.__positions__[row][col]
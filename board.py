from rook import Rook
from pawn import Pawn
from queen import Queen
from king import King

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        
        # Ponemos las torres en las esquinas
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
            
        # Colocar las reinas
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")
        
        # Colocar los reyes
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")
        
    def get_piece(self, row, col):
        return self.__positions__[row][col]
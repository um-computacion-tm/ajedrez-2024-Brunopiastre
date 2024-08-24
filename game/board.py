from game.rook import Rook
from game.pawn import Pawn
from game.queen import Queen
from game.king import King
from game.knight import Knight
from game.bishop import Bishop

class Board:
    def __init__(self, positions=None):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        
        # Ponemos las torres en las esquinas
        self.__positions__[0][0] = Rook("BLACK", (0, 0))
        self.__positions__[0][7] = Rook("BLACK", (0, 7))
        self.__positions__[7][0] = Rook("WHITE", (7, 0))
        self.__positions__[7][7] = Rook("WHITE", (7, 7))
        
        
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
        
        # Colocar los caballos
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")
        
        # Colocar los alfiles
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")
        
    def get_piece(self, row, col):
        return self.__positions__[row][col]
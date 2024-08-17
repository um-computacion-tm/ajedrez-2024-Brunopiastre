from board import Board
from piece import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        # Verifica coordenadas

        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            print("No hay pieza en la posición de origen.")
            return False

        if not piece.move((from_row, from_col), (to_row, to_col)):
            print("Movimiento inválido para la pieza.")
            return False    

        destination_piece = self.__board__.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.color == piece.color:
            print("Ya existe una pieza en esta posición.")
            return False

        # Mover la pieza
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        self.change_turn()
        return True

    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
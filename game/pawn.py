from game.piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type_of_movement = "forward one square"

    def get_type_of_movement(self):
        return self.type_of_movement
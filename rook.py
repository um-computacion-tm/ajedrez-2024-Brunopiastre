from piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type_of_movement = "horizontal and vertical"

    def get_type_of_movement(self):
        return self.type_of_movement

import unittest
from game.pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_pawn_attributes(self):
        pawn_black = Pawn("BLACK")
        pawn_white = Pawn("WHITE")

        # Verificar el color
        self.assertEqual(pawn_black.color, "BLACK")
        self.assertEqual(pawn_white.color, "WHITE")

        # Verificar el tipo de movimiento
        self.assertEqual(pawn_black.get_type_of_movement(), "forward one square")
        self.assertEqual(pawn_white.get_type_of_movement(), "forward one square")

if __name__ == '__main__':
    unittest.main()
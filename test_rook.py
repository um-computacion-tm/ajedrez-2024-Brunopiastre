import unittest
from rook import Rook

class TestRook(unittest.TestCase):

    def test_rook_attributes(self):
        rook_black = Rook("BLACK")
        rook_white = Rook("WHITE")

        # Verificar el color
        self.assertEqual(rook_black.color, "BLACK")
        self.assertEqual(rook_white.color, "WHITE")

        # Verificar el tipo de movimiento
        self.assertEqual(rook_black.get_type_of_movement(), "horizontal and vertical")
        self.assertEqual(rook_white.get_type_of_movement(), "horizontal and vertical")

if __name__ == '__main__':
    unittest.main()
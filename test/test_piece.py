import unittest
from game.piece import Piece

class PieceTestCase(unittest.TestCase):
    def test_init(self):
        # Test case 1: Creating a white piece
        piece = Piece("WHITE")
        self.assertEqual(piece.color, "WHITE")

        # Test case 2: Creating a black piece
        piece = Piece("BLACK")
        self.assertEqual(piece.color, "BLACK")

if __name__ == "__main__":
    unittest.main()
import unittest
from game.board import Board
from game.rook import Rook

class TestRook(unittest.TestCase):
    def test_rook_color(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♜")
        
        rook = Rook("BLACK")
        self.assertEqual(str(rook), "♖")

if __name__ == '__main__':
    unittest.main()
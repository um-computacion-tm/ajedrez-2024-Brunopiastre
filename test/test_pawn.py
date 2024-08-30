import unittest
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_str_white(self):
        pawn = Pawn("WHITE")
        self.assertEqual(str(pawn), "♙")

    def test_str_black(self):
        pawn = Pawn("BLACK")
        self.assertEqual(str(pawn), "♟")

if __name__ == "__main__":
    unittest.main()
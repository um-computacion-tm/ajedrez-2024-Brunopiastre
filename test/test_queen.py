import unittest
from game.queen import Queen

class TestQueen(unittest.TestCase):
    def test_str_white(self):
        queen = Queen("WHITE")
        self.assertEqual(str(queen), "♕")

    def test_str_black(self):
        queen = Queen("BLACK")
        self.assertEqual(str(queen), "♛")

if __name__ == "__main__":
    unittest.main()
import unittest
from game.king import King

class TestKing(unittest.TestCase):
    def test_str_white(self):
        king = King("WHITE")
        self.assertEqual(str(king), "♔")

    def test_str_black(self):
        king = King("BLACK")
        self.assertEqual(str(king), "♚")

if __name__ == '__main__':
    unittest.main()
import unittest
from game.bishop import Bishop

class TestBishop(unittest.TestCase):
    def test_str_white(self):
        bishop = Bishop("WHITE")
        self.assertEqual(str(bishop), "♗")

    def test_str_black(self):
        bishop = Bishop("BLACK")
        self.assertEqual(str(bishop), "♝")

if __name__ == "__main__":
    unittest.main()
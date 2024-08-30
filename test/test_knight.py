import unittest
from game.knight import Knight

class KnightTests(unittest.TestCase):
    def test_str_white(self):
        knight = Knight("WHITE")
        self.assertEqual(str(knight), "♘")

    def test_str_black(self):
        knight = Knight("BLACK")
        self.assertEqual(str(knight), "♞")

if __name__ == "__main__":
    unittest.main()
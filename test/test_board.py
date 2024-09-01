import unittest
from game.board import Board
from game.rook import Rook
from game.pawn import Pawn
from game.queen import Queen
from game.king import King
from game.knight import Knight
from game.bishop import Bishop

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        
    def test_initial_positions_rook(self):
        # Verificar que las torres negras estén en las posiciones correctas
        self.assertEqual(self.board.__positions__[0][0].color, "WHITE")

    def test_empty_positions(self):
        # Verificar que las posiciones vacías sean None
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col))
                
    def test_positions(self):
        self.assertEqual(self.board.get_piece(0, 0), "WHITE")
       
       
    def test_show_board(self):
        expected_output = "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n" \
                          "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n" \
                          ". . . . . . . .\n" \
                          ". . . . . . . .\n" \
                          ". . . . . . . .\n" \
                          ". . . . . . . .\n" \
                          "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" \
                          "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖"
        self.assertEqual(expected_output, self.board.show_board())
               

if __name__ == '__main__':
    unittest.main()
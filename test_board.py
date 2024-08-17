import unittest
from board import Board
from rook import Rook
from pawn import Pawn

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        
    def test_initial_positions(self):
        # Verificar que las torres negras estén en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
        
    # Verificar que las torres blancas estén en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")
        
        
    # Verificar que los peones negros estén en las posiciones correctas
        for i in range(8):
            self.assertIsInstance(self.board.get_piece(1, i), Pawn)
            self.assertEqual(self.board.get_piece(1, i).color, "BLACK")
        
        # Verificar que los peones blancos estén en las posiciones correctas
        for i in range(8):
            self.assertIsInstance(self.board.get_piece(6, i), Pawn)
            self.assertEqual(self.board.get_piece(6, i).color, "WHITE")

        
    def test_empty_positions(self):
            # Verificar que las posiciones vacías sean None
            self.assertIsNone(self.board.get_piece(1, 1))
            self.assertIsNone(self.board.get_piece(6, 6))


    
if __name__ == '__main__':
    unittest.main()
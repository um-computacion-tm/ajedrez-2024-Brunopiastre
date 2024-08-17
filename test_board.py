import unittest
from board import Board
from rook import Rook
from pawn import Pawn
from queen import Queen
from king import King

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
        
        # Verificar que las reinas estén en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertEqual(self.board.get_piece(0, 3).color, "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertEqual(self.board.get_piece(7, 3).color, "WHITE")
        
        # Verificar que los reyes estén en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertEqual(self.board.get_piece(0, 4).color, "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertEqual(self.board.get_piece(7, 4).color, "WHITE")
        
        # Pruebas negativas: Verificar que las piezas no estén en posiciones incorrectas
        self.assertIsNone(self.board.get_piece(0, 1))  # No debería haber pieza en (0, 1)
        self.assertIsNone(self.board.get_piece(7, 1))  # No debería haber pieza en (7, 1)
        self.assertIsNone(self.board.get_piece(1, 0))  # No debería haber pieza en (1, 0) que no sea un peón
        self.assertIsNone(self.board.get_piece(6, 0))  # No debería haber pieza en (6, 0) que no sea un peón
        
    def test_empty_positions(self):
        # Verificar que las posiciones vacías sean None
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()
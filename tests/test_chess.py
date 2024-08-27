import unittest
from unittest.mock import patch
from game.chess import Chess
from game.board import Board
from game.piece import Piece

class TestChess(unittest.TestCase):
    
    def test_init(self):
        self.assertEqual(1, 1)

    # @patch('chess.Board.get_piece', return_value=None)
    # @patch('builtins.print')
    # def test_no_piece_in_origin(self, mock_print, mock_get_piece):
    #     juego = Chess()
    #     result = juego.move(0, 0, 1, 1)
        
    #     # Verificar que el método retorna False
    #     self.assertFalse(result)
        
    #     # Verificar que se imprimió el mensaje correcto
    #     mock_print.assert_called_with("No hay pieza en la posición de origen.")
    
    # @patch('chess.Board.get_piece')
    # @patch('builtins.print')
    # def test_move_out_of_range(self, mock_print, mock_get_piece):
    #     juego = Chess()
    #     result = juego.move(-1, 0, 1, 1)
        
    #     # Verificar que el método retorna False
    #     self.assertFalse(result)
        
    #     # Verificar que se imprimió el mensaje correcto
    #     mock_print.assert_called_with("Coordenadas fuera de rango.")    
    
    # @patch('chess.Board.get_piece')
    # @patch('builtins.print')
    # def test_invalid_move(self, mock_print, mock_get_piece):
    #     juego = Chess()
    #     piece = Piece("WHITE")
    #     piece.move = lambda from_pos, to_pos: False
    #     mock_get_piece.return_value = piece
    #     result = juego.move(0, 0, 1, 1)
        
    #     # Verificar que el método retorna False
    #     self.assertFalse(result)
    
    if __name__ == '__main__':
        unittest.main()
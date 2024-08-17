import unittest
from unittest.mock import patch
from chess import Chess, Board, Piece

class TestChess(unittest.TestCase):

    @patch('chess.Board.get_piece', return_value=None)
    @patch('builtins.print')
    def test_no_piece_in_origin(self, mock_print, mock_get_piece):
        juego = Chess()
        result = juego.move(0, 0, 1, 1)
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("No hay pieza en la posición de origen.")
    
    @patch('chess.Board.get_piece')
    @patch('builtins.print')
    def test_move_out_of_range(self, mock_print, mock_get_piece):
        juego = Chess()
        result = juego.move(-1, 0, 1, 1)
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("Coordenadas fuera de rango.")    
    
    @patch('chess.Board.get_piece')
    @patch('builtins.print')
    def test_invalid_move(self, mock_print, mock_get_piece):
        juego = Chess()
        piece = Piece("WHITE")
        piece.move = lambda from_pos, to_pos: False
        mock_get_piece.return_value = piece
        result = juego.move(0, 0, 1, 1)
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("Movimiento inválido para la pieza.")
    
    @patch('chess.Board.get_piece')
    @patch('builtins.print')
    def test_capture_own_piece(self, mock_print, mock_get_piece):
        juego = Chess()
        piece = Piece("WHITE")
        piece.move = lambda from_pos, to_pos: True
        #hace que exista una pieza blanza en el destino y en el origen
        mock_get_piece.side_effect = [piece, piece]
        result = juego.move(0, 0, 1, 1)
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("No podes comer tu propia pieza.")
    
    @patch('chess.Board.get_piece')
    @patch('chess.Board.move_piece')
    def test_valid_move(self, mock_move_piece, mock_get_piece):
        juego = Chess()
        piece = Piece("WHITE")
        piece.move = lambda from_pos, to_pos: True
        mock_get_piece.side_effect = [piece, None]
        result = juego.move(0, 0, 1, 1)
        
        # Verificar que el método retorna True
        self.assertTrue(result)
        
        # Verificar que se llamó a move_piece
        mock_move_piece.assert_called_with(0, 0, 1, 1)
    
    @patch('chess.Board.get_piece')
    @patch('chess.Board.move_piece')
    def test_turn_change(self, mock_move_piece, mock_get_piece):
        juego = Chess()
        piece = Piece("WHITE")
        piece.move = lambda from_pos, to_pos: True
        mock_get_piece.side_effect = [piece, None]
        juego.move(0, 0, 1, 1)
        
        # Verificar que el turno cambió a BLACK
        self.assertEqual(juego.turn, "BLACK")
        
        # Realizar otro movimiento para cambiar el turno de nuevo
        piece_black = Piece("BLACK")
        piece_black.move = lambda from_pos, to_pos: True
        mock_get_piece.side_effect = [piece_black, None]
        juego.move(1, 1, 2, 2)
        
        # Verificar que el turno cambió a WHITE
        self.assertEqual(juego.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()
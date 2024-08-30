import unittest
from game.chess import Chess
from game.chess import InvalidMove
from game.chess import InvalidMoveNoPiece
from game.chess import InvalidMoveRookMove

class TestInvalidMove(unittest.TestCase):
    def test_default_message(self):
        exception = InvalidMove()
        self.assertEqual(str(exception), "Movimiento inválido")

    def test_custom_message(self):
        custom_message = "Movimiento no permitido"
        exception = InvalidMove(custom_message)
        self.assertEqual(str(exception), custom_message)
class TestInvalidMoveNoPiece(unittest.TestCase):
    def test_default_message(self):
        exception = InvalidMoveNoPiece()
        self.assertEqual(str(exception), "No hay pieza en la posición de origen")
    def test_custom_message(self):
        custom_message = "No hay pieza en la posición especificada"
        exception = InvalidMoveNoPiece(custom_message)
        self.assertEqual(str(exception), custom_message)
class TestInvalidMoveRookMove(unittest.TestCase):
    def test_default_message(self):
        exception = InvalidMoveRookMove()
        self.assertEqual(str(exception), "Movimiento inválido para la torre")

    def test_custom_message(self):
        custom_message = "Movimiento no permitido para la torre"
        exception = InvalidMoveRookMove(custom_message)
        self.assertEqual(str(exception), custom_message)
        
class TestChess(unittest.TestCase):
    def test_initial_turn(self):
        # Crear una instancia de la clase Chess
        chess_game = Chess()
        # Verificar que el turno inicial sea "WHITE"
        self.assertEqual(chess_game.__turn__, "WHITE")
    
    def test_is_playing(self):
        chess_game = Chess()
        self.assertTrue(chess_game.is_playing())

    # def test_move_invalid(self):
    #     chess_game = Chess()
    #     with self.assertRaises(InvalidMove):
    #         chess_game.move(0, 0, 1, 1)
        
    # def test_move_valid(self):
    #     chess_game = Chess()
    #     chess_game.move(1, 0, 2, 0)
    #     self.assertEqual(chess_game.turn, "BLACK")
    
    
    def test_initial_turn(self):
        chess_game = Chess()
        self.assertEqual(chess_game.turn, "WHITE")

    def test_change_turn(self):
        chess_game = Chess()
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "BLACK")
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "WHITE")


    def test_show_board(self):
        chess_game = Chess()
        expected_board = str(chess_game.__board__)
        self.assertEqual(chess_game.show_board(), expected_board)

if __name__ == "__main__":
    unittest.main()
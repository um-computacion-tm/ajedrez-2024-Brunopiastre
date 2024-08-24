# import unittest
# from game.board import Board
# from game.rook import Rook
# from game.pawn import Pawn
# from game.queen import Queen
# from game.king import King
# from game.knight import Knight
# from game.bishop import Bishop

# class TestBoard(unittest.TestCase):
    
#     def setUp(self):
#         self.board = Board()
        
#     def test_initial_positions(self):
#         # Verificar que las torres negras estén en las posiciones correctas
#         self.assertIsInstance(self.board.get_piece(0, 0), Rook)
#         self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(0, 7), Rook)
#         self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
        
#         # Verificar que las torres blancas estén en las posiciones correctas
#         self.assertIsInstance(self.board.get_piece(7, 0), Rook)
#         self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
#         self.assertIsInstance(self.board.get_piece(7, 7), Rook)
#         self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")
        
#         # Verificar que los peones negros estén en las posiciones correctas
#         for i in range(8):
#             self.assertIsInstance(self.board.get_piece(1, i), Pawn)
#             self.assertEqual(self.board.get_piece(1, i).color, "BLACK")
        
#         # Verificar que los peones blancos estén en las posiciones correctas
#         for i in range(8):
#             self.assertIsInstance(self.board.get_piece(6, i), Pawn)
#             self.assertEqual(self.board.get_piece(6, i).color, "WHITE")
        
#         # Verificar que las reinas estén en las posiciones correctas
#         self.assertIsInstance(self.board.get_piece(0, 3), Queen)
#         self.assertEqual(self.board.get_piece(0, 3).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(7, 3), Queen)
#         self.assertEqual(self.board.get_piece(7, 3).color, "WHITE")
        
#         # Verificar que los reyes estén en las posiciones correctas
#         self.assertIsInstance(self.board.get_piece(0, 4), King)
#         self.assertEqual(self.board.get_piece(0, 4).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(7, 4), King)
#         self.assertEqual(self.board.get_piece(7, 4).color, "WHITE")
        
#         # Verificar que los caballos estén en las posiciones correctas
#         self.assertIsInstance(self.board.get_piece(0, 1), Knight)
#         self.assertEqual(self.board.get_piece(0, 1).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(0, 6), Knight)
#         self.assertEqual(self.board.get_piece(0, 6).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(7, 1), Knight)
#         self.assertEqual(self.board.get_piece(7, 1).color, "WHITE")
#         self.assertIsInstance(self.board.get_piece(7, 6), Knight)
#         self.assertEqual(self.board.get_piece(7, 6).color, "WHITE")
        
#         # Verificar que los alfiles estén en las posiciones correctas
#         self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
#         self.assertEqual(self.board.get_piece(0, 2).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
#         self.assertEqual(self.board.get_piece(0, 5).color, "BLACK")
#         self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
#         self.assertEqual(self.board.get_piece(7, 2).color, "WHITE")
#         self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
#         self.assertEqual(self.board.get_piece(7, 5).color, "WHITE")
        
#     def test_negative_positions(self):
#         # Pruebas negativas: Verificar que las piezas no estén en posiciones incorrectas
#         # Torres
#         self.assertIsNone(self.board.get_piece(0, 1))  # No debería haber torre en (0, 1)
#         self.assertIsNone(self.board.get_piece(7, 1))  # No debería haber torre en (7, 1)
        
#         # Peones
#         self.assertIsNone(self.board.get_piece(0, 2))  # No debería haber peón en (0, 2)
#         self.assertIsNone(self.board.get_piece(7, 2))  # No debería haber peón en (7, 2)
        
#         # Reinas
#         self.assertIsNone(self.board.get_piece(0, 0))  # No debería haber reina en (0, 0)
#         self.assertIsNone(self.board.get_piece(7, 0))  # No debería haber reina en (7, 0)
        
#         # Reyes
#         self.assertIsNone(self.board.get_piece(0, 1))  # No debería haber rey en (0, 1)
#         self.assertIsNone(self.board.get_piece(7, 1))  # No debería haber rey en (7, 1)
        
#         # Caballos
#         self.assertIsNone(self.board.get_piece(0, 0))  # No debería haber caballo en (0, 0)
#         self.assertIsNone(self.board.get_piece(7, 0))  # No debería haber caballo en (7, 0)
        
#         # Alfiles
#         self.assertIsNone(self.board.get_piece(0, 0))  # No debería haber alfil en (0, 0)
#         self.assertIsNone(self.board.get_piece(7, 0))  # No debería haber alfil en (7, 0)
        
#     def test_empty_positions(self):
#         # Verificar que las posiciones vacías sean None
#         for row in range(2, 6):
#             for col in range(8):
#                 self.assertIsNone(self.board.get_piece(row, col))

# if __name__ == '__main__':
#     unittest.main()
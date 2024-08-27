# from game.piece import Piece

# class Rook(Piece):
#     def __init__(self, color, posicion):
#         super().__init__(color, position)

#     def movimientos_validos(self, board):
#         movimientos = []
#         x, y = self.position
    
#         # Movimientos verticales hacia arriba
#         for i in range(x - 1, -1, -1):
#             if board[i][y] is None:
#                 movimientos.append((i, y))
#             else:
#                 if board[i][y].color != self.color:
#                     movimientos.append((i, y))
#                 break
            
#         # Movimientos verticales hacia abajo
#         for i in range(x + 1, 8):
#             if board[i][y] is None:
#                 movimientos.append((i, y))
#             else:
#                 if board[i][y].color != self.color:
#                     movimientos.append((i, y))
#                 break
            
#         # Movimientos horizontales hacia la izquierda
#         for j in range(y - 1, -1, -1):
#             if board[x][j] is None:
#                 movimientos.append((x, j))
#             else:
#                 if board[x][j].color != self.color:
#                     movimientos.append((x, j))
#                 break
            
#         # Movimientos horizontales hacia la derecha
#         for j in range(y + 1, 8):
#             if board[x][j] is None:
#                 movimientos.append((x, j))
#             else:
#                 if board[x][j].color != self.color:
#                     movimientos.append((x, j))
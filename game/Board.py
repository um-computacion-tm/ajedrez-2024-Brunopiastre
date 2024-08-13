class Board:
    def __init__(self):
        self.positions = []
        
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)  # O el valor que desees para cada posición
              self.positions.append [0] [0] = Rook Black 
           self.positions.append [7] [7] = Rook white 
            
            
        self.positions[0][0] = Rook('black')

# Ejemplo de uso
board = Board()
print(board.positions)

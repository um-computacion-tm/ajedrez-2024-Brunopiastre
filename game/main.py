from game.chess import Chess

def main():
    while True:
        print("Bienvenido al juego de Ajedrez")
        print("1. Nueva partida")
        print("2. Instrucciones")
        print("3. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            start_game()
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige de nuevo.")


def start_game():
    chess = Chess()
    while chess.is_playing():
        play(chess)


def show_instructions():
    print("Instrucciones del juego de Ajedrez:")
    print("1. El objetivo del juego es dar jaque mate al rey del oponente.")
    print("2. Cada tipo de pieza se mueve de manera diferente:")
    print("   - Peones: se mueven hacia adelante pero capturan en diagonal.")
    print("   - Torres: se mueven en línea recta horizontal o verticalmente.")
    print("   - Caballos: se mueven en forma de 'L'.")
    print("   - Alfiles: se mueven en diagonal.")
    print("   - Reina: se mueve en cualquier dirección.")
    print("   - Rey: se mueve una casilla en cualquier dirección.")
    print("3. Los jugadores se turnan para mover una pieza a la vez.")
    print("4. No puedes mover una pieza a una casilla ocupada por una pieza del mismo color.")
    print("5. Si mueves una pieza a una casilla ocupada por una pieza del oponente, capturas esa pieza.")
    print("6. El juego termina cuando un rey está en jaque mate, no puede moverse a una casilla segura.")
    print("7. Para mover una pieza, ingresa las coordenadas de origen y destino.")
    print("8. ¡Diviértete jugando!")

def play(chess):
    try:
        chess.show_board()
        print("Turno: ", chess.turn)
        from_row = int(input("Desde fila: "))
        from_col = int(input("Desde columna: "))
        to_row = int(input("Hasta fila: "))
        to_col = int(input("Hasta columna: "))
        
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
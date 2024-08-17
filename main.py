from board import Board

class Main:
    def main(self):
        while True:
            print("--Ajedrez--")
            print("1. Seleccionar color de sus piezas")
            print("2. Iniciar nueva partida")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.seleccionar_color()
            elif opcion == "2":
                self.iniciar_partida()
            elif opcion == "3":
                print("Saliendo del juego...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def seleccionar_color(self):
        color = input("Seleccione el color de sus piezas (blanco/negro): ")
        if color.lower() in ["blanco", "negro"]:
            print(f"Has seleccionado el color {color}.")
        else:
            print("Color no válido. Por favor, intente de nuevo.")

    def iniciar_partida(self):
        print("Iniciando nueva partida...")

if __name__ == "__main__":
    juego = Main()
    juego.main()
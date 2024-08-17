import unittest
from unittest.mock import patch
from main import Main

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'blanco', '3'])
    def test_seleccionar_color_blanco(self, mock_input):
        with patch('builtins.print') as mock_print:
            juego = Main()
            juego.main()
            mock_print.assert_any_call("Seleccione el color de sus piezas (blanco/negro): ")
            mock_print.assert_any_call("Has seleccionado el color blanco.")
            mock_print.assert_any_call("Saliendo del juego...")

    @patch('builtins.input', side_effect=['1', 'negro', '3'])
    def test_seleccionar_color_negro(self, mock_input):
        with patch('builtins.print') as mock_print:
            juego = Main()
            juego.main()
            mock_print.assert_any_call("Seleccione el color de sus piezas (blanco/negro): ")
            mock_print.assert_any_call("Has seleccionado el color negro.")
            mock_print.assert_any_call("Saliendo del juego...")

    @patch('builtins.input', side_effect=['2', '3'])
    def test_iniciar_nueva_partida(self, mock_input):
        with patch('builtins.print') as mock_print:
            juego = Main()
            juego.main()
            mock_print.assert_any_call("Iniciando nueva partida...")
            mock_print.assert_any_call("Saliendo del juego...")

    @patch('builtins.input', side_effect=['3'])
    def test_salir(self, mock_input):
        with patch('builtins.print') as mock_print:
            juego = Main()
            juego.main()
            mock_print.assert_any_call("Saliendo del juego...")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import MagicMock
from controllers.user_controller import UserController

class TestUserController(unittest.TestCase):

    def setUp(self):
        self.controller = UserController()
        self.controller.dao = MagicMock()

    def test_listar_usuarios(self):
        self.controller.dao.obtener_todos.return_value = [(1, "Juan", "juan@gmail.com")]

        usuarios = self.controller.listar_usuarios()

        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0][1], "Juan")

    def test_agregar_usuario(self):
        self.controller.agregar_usuario("Ana", "ana@gmail.com")
        self.controller.dao.insertar.assert_called_once_with("Ana", "ana@gmail.com")

    def test_eliminar_usuario(self):
        self.controller.eliminar_usuario(1)
        self.controller.dao.eliminar.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()
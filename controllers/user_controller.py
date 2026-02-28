from dao.user_dao import UserDAO

class UserController:

    def __init__(self):
        self.dao = UserDAO()

    def listar_usuarios(self):
        return self.dao.obtener_todos()

    def agregar_usuario(self, name, email):
        self.dao.insertar(name, email)

    def editar_usuario(self, id, name, email):
        self.dao.actualizar(id, name, email)

    def eliminar_usuario(self, id):
        self.dao.eliminar(id)
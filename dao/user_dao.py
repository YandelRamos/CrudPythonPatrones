from config.conexion import Conexion

class UserDAO:

    def __init__(self):
        self.conexion = Conexion().obtener_conexion()
        self.cursor = self.conexion.cursor()

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def insertar(self, name, email):
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        valores = (name, email)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def actualizar(self, id, name, email):
        sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        valores = (name, email, id)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def eliminar(self, id):
        sql = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.conexion.commit()
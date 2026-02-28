import mysql.connector

class Conexion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crudpython"
            )
        return cls._instancia

    def obtener_conexion(self):
        return self.conexion
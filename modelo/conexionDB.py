import sqlite3

class conexionDB:
    def _init_(self):
        self.baseDatos = './AppCitas/Database/historial.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()
    
    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()
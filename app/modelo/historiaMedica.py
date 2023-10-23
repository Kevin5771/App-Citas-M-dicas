from sqlite3.dbapi2 import Cursor
from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoria, p.nombre || " " || p.apellido|| " " || AS Apellidos, h.fecha, h.motivo, h.tratamiento, h.detalle FROM historia h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)

    return listaHistoria

def guardarHistoria(idPersona, fechaHistoria, motivo, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historia (idPersona, fecha, motivo, tratamiento, detalle) VALUES
            ({idPersona},'{fechaHistoria}','{motivo}','{tratamiento}','{detalle}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Medica'
        mensaje = 'Historia registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historia Medica'
        mensaje = 'Error al registrar historia'
        messagebox.showerror(title, mensaje)

def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historia WHERE idHistoria = {idHistoriaMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia medica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia medica'
        messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistoria, motivo, tratamiento, detalle, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""UPDATE historia SET fechaHistoria = '{fechaHistoria}', motivo = '{motivo}', tratamiento = '{tratamiento}', detalle = '{detalle}' WHERE idHistoria = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historia'
        mensaje = 'Historia medica editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Historia'
        mensaje = 'Error al editar historia medica'
        messagebox.showerror(title, mensaje)

class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, tratamiento, detalle):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.tratamiento = tratamiento
        self.detalle = detalle
    
    def __str__(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivo}, {self.tratamiento}, {self.detalle}]'
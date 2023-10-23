
from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE PERSONA SET nombre = '{persona.nombre}', apellido = '{persona.apellido}',
            dpi = '{persona.dpi}', fechaCita = '{persona.fechaCita}', edad = {persona.edad}, 
            correo = '{persona.cOrreo}', telefono = '{persona.telefono}', motivo = '{persona.motivo}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar paciente'
        messagebox.showinfo(title, mensaje)

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellido, dpi, fechaCita, 
    edad, cOrreo, telefono,motivo,activo) VALUES
            ('{persona.nombre}','{persona.apellido}','{persona.dpi}',
            '{persona.fechaCita}',{persona.edad},
            '{persona.cOrreo}','{persona.telefono}','{persona.motivo}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showerror(title,mensaje)

def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona


def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona


def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title, mensaje)


class Persona:
    def __init__(self, nombre, apellido, dpi,fechaCita, edad, cOrreo, telefono,motivo):
        self.idPersona = None
        self.nombre = nombre
        self.apellido= apellido
        self.dpi = dpi
        self.fechaCita = fechaCita
        self.edad = edad
        self.cOrreo = cOrreo
        self.telefono = telefono
        self.motivo = motivo

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellido}, {self.dpi},{self.fechaCita},{self.edad},{self.cOrreo},{self.telefono},{self.motivo}]'
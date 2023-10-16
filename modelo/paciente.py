from .conexionDB import conexionDB
from tkinter import messagebox


def guardarDato(Persona):
    conexio = conexionDB()
    sql= f"""INSERT INTO Persona(nombre,apellido,dpi,fechaCita,edad,c0rreo,telefono, activo)
    VALUES('{Persona.nombre}', '{Persona.apellido}',{Persona.dpi},'{Persona.FachaCita}',
    {Persona.edad},'{Persona.c0rreo}','{Persona.telefono}',1)"""
    try:
        conexio.cursor.execute(sql)
        conexio.cerrarConexion()
        title= 'Registar Paciente'
        mensaje ='Paciente Registrado Exitosamente'
        messagebox.showinfo(title,mensaje)
    except:
        title= 'Registrar Paciente'
        mensaje='Error al Registar el Paciente'
        messagebox.showerror(title,mensaje)

class Persona:
    def __init__(self, nombre, apellido, dpi, fechaCita, edad, c0rreo, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellido = apellido
        self.dpi = dpi
        self.fechaCita = fechaCita
        self.edad = edad
        self.correo = c0rreo
        self.telefono = telefono
    
    def __str__(self):
        return f'Persona[{self.nombre},{self.apellido},{self.dpi},{self.fechaCita},{self.edad},{self.correo}, {self.telefono}]'
    
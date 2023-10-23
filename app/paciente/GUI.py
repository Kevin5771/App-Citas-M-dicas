from calendar import LocaleHTMLCalendar
from os import P_DETACH
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame, StringVar
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaMedica = None
        self.idHistoriaMedicaEditar = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def camposPaciente(self):

        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApellido = tk.Label(self, text='Apellido: ')
        self.lblApellido.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblApellido.grid(column=0,row=1, padx=10, pady=5)

        self.lblDpi = tk.Label(self, text='DPI: ')
        self.lblDpi.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblDpi.grid(column=0,row=2, padx=10, pady=5)

        self.lblFechaCita = tk.Label(self, text='Fecha cita: ')
        self.lblFechaCita.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblFechaCita.grid(column=0,row=3, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0,row=4, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0,row=5, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0,row=6, padx=10, pady=5)  

        self.lblMotivo = tk.Label(self, text='Motivo: ')
        self.lblMotivo.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblMotivo.grid(column=0,row=7, padx=10, pady=5)  


        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellido= tk.StringVar()
        self.entryApellido= tk.Entry(self, textvariable=self.svApellido)
        self.entryApellido.config(width=50, font=('ARIAL',15))
        self.entryApellido.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDPI = tk.StringVar()
        self.entryDPI = tk.Entry(self, textvariable=self.svDPI)
        self.entryDPI.config(width=50, font=('ARIAL',15))
        self.entryDPI.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFechaCita = tk.StringVar()
        self.entryFechaCita = tk.Entry(self, textvariable=self.svFechaCita)
        self.entryFechaCita.config(width=50, font=('ARIAL',15))
        self.entryFechaCita.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL',15))
        self.entryCorreo.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL',15))
        self.entryTelefono.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svMotivoCita = tk.StringVar()
        self.entryMotivo = tk.Entry(self, textvariable=self.svMotivoCita)
        self.entryMotivo.config(width=50, font=('ARIAL',15))
        self.entryMotivo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)


        #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#5718de', cursor='hand2',activebackground='#880bdb')
        self.btnNuevo.grid(column=0,row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#000000', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1,row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar',command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=2,row=9, padx=10, pady=5)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarFechaCita = tk.Label(self, text='Buscar Fechas: ')
        self.lblBuscarFechaCita.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblBuscarFechaCita.grid(column=3, row=1, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblBuscarApellido.grid(column=3, row=2, padx=10, pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarFechaCita = tk.StringVar()
        self.entryBuscarFechaCita = tk.Entry(self, textvariable=self.svBuscarFechaCita)
        self.entryBuscarFechaCita.config(width=20, font=('ARIAL',15))
        self.entryBuscarFechaCita.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20, font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4, row=2, padx=10, pady=5, columnspan=2)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command = self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#4352c4')
        self.btnBuscarCondicion.grid(column=3,row=3, padx=10, pady=5, columnspan=1)

        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command = self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnLimpiarBuscador.grid(column=4,row=3, padx=10, pady=5, columnspan=1)
# 
        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command = self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#53005B', cursor='hand2',activebackground='#C774CF')
        self.btnCalendario.grid(column=3,row=5, padx=10, pady=5, columnspan=1)
        
# Necesita Correcciones

    def vistaCalendario(self):
        self.topCalendario = Toplevel()
        self.topCalendario.title("FECHA CITA")
        self.topCalendario.resizable(0, 0)
        self.topCalendario.iconbitmap('./app/img/clinica.ico')
        self.topCalendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar()
        self.svCalendario.set("01-10-2023")  # Establecer una fecha predeterminada en formato "dd-mm-yyyy"
        
        self.calendar = tc.Calendar(self.topCalendario, selectmode='day', locale='es_US', bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE', textvariable=self.svCalendario, cursor='hand2', date_pattern='dd-mm-Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column=0)

        # TRACE ENVIAR FECHA
        self.svCalendario.trace_add('write', self.enviarFecha)

    def enviarFecha(self, *args):
        fecha_seleccionada = self.svCalendario.get()
        
    #Función de Botones para busquedas
    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarFechaCita.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        where = "WHERE activo = 1"
        if len(self.svBuscarFechaCita.get()) > 0:
            where += " AND FechaCita = '" + self.svBuscarFechaCita.get() + "'"
        if len(self.svBuscarApellido.get()) > 0:
            where += " AND apellido LIKE '" + self.svBuscarApellido.get() + "%'"

        self.tablaPaciente(where)


    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApellido.get(),
            self.svDPI.get(), self.svFechaCita.get(), self.svEdad.get(), 
            self.svCorreo.get(), self.svTelefono.get(), self.svMotivoCita.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

        self.deshabilitar()
        self.tablaPaciente()
        # self.topCalendario.destroy()

    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDPI.set('')
        self.svFechaCita.set('')
        self.svEdad.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        self.svMotivoCita.set('')

        self.entryNombre.config(state='normal')
        self.entryApellido.config(state='normal')
        self.entryDPI.config(state='normal')
        self.entryFechaCita.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')
        self.entryMotivo.config(state="normal")

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDPI.set('')
        self.svFechaCita.set('')
        self.svEdad.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        self.svMotivoCita.set('')

        self.entryNombre.config(state='disabled')
        self.entryApellido.config(state='disabled')
        self.entryDPI.config(state='disabled')
        self.entryFechaCita.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        self.entryMotivo.config(state="disabled")

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apellido','Dpi','FCita','Edad','Correo','Telefono', 'Motivo'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='DPI')
        self.tabla.heading('#4',text='F. Cita')
        self.tabla.heading('#5',text='Edad')
        self.tabla.heading('#6',text='Correo')
        self.tabla.heading('#7',text='Telefono')
        self.tabla.heading('#8',text='Motivo')

        self.tabla.column("#0", anchor=W, width=75)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=150)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=120)
        self.tabla.column("#5", anchor=W, width=80)
        self.tabla.column("#6", anchor=W, width=210)
        self.tabla.column("#7", anchor=W, width=120)
        self.tabla.column("#8", anchor=W, width=235)

        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]), tags=('evenrow',))

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command = self.eliminarDatoPaciente )
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=11, column=4, padx=10, pady=5)

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.dpiPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.fechaCitaPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.motivoCitaPaciente = self.tabla.item(self.tabla.selection())['values'][7]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApellido.insert(0, self.apellidoPaciente)
            self.entryDPI.insert(0, self.dpiPaciente)
            self.entryFechaCita.insert(0, self.fechaCitaPaciente)
            self.entryEdad.insert(0,self.edadPaciente)
            self.entryCorreo.insert(0,self.correoPaciente)
            self.entryTelefono.insert(0,self.telefonoPaciente)
            self.entryMotivo.insert(0,self.motivoCitaPaciente)

        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)
    
    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)
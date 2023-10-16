import tkinter as tk
from modelo.paciente import Persona, guardarDato

class Frame(tk.Frame):
    def __init__(self,root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#B0D9F4')
        self.paciente()

    def paciente(self):
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApellido = tk.Label(self, text='Apellido: ')
        self.lblApellido.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblApellido.grid(column=0, row=1, padx=10, pady=5)

        self.lblDpi = tk.Label(self, text='DPI: ')
        self.lblDpi.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblDpi.grid(column=0, row=2, padx=10, pady=5)

        self.lblFechaCita = tk.Label(self, text='Fecha de su Cita: ')
        self.lblFechaCita.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblFechaCita.grid(column=0, row=3, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblEdad.grid(column=0, row=4, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblCorreo.grid(column=0, row=5, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Teléfono: ')
        self.lblTelefono.config(font=('ARIAL', 15, 'bold'), bg='#B0D9F4')
        self.lblTelefono.grid(column=0, row=6, padx=10, pady=5)

        #Datos de Entradas
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL', 15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellido = tk.StringVar()
        self.entryApellido = tk.Entry(self, textvariable=self.svApellido)
        self.entryApellido.config(width=50, font=('ARIAL', 15))
        self.entryApellido.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDpi = tk.StringVar()
        self.entryDpi = tk.Entry(self, textvariable=self.svDpi)
        self.entryDpi.config(width=50, font=('ARIAL', 15))
        self.entryDpi.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFechaCita = tk.StringVar()
        self.entryFechaCita = tk.Entry(self, textvariable=self.svFechaCita)
        self.entryFechaCita.config(width=50, font=('ARIAL', 15))
        self.entryFechaCita.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL', 15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL', 15))
        self.entryCorreo.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL', 15))
        self.entryTelefono.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        #Botones interactivos
        self.btnNuevo = tk.Button(self, text='Nuevo')
        self.btnNuevo.config(width=20, font=('ARIAL', 12, 'bold'), fg='white', bg='#2310E8', cursor='hand2', activebackground='#796DF1')
        self.btnNuevo.grid(column=0, row=7, padx=10, pady=5)        

        self.btnGuardar = tk.Button(self, text='Guardar')
        self.btnGuardar.config(width=20, font=('ARIAL', 12, 'bold'), fg='white', bg='#000000', cursor='hand2', activebackground='#3F5F5F')
        self.btnGuardar.grid(column=1, row=7, padx=10, pady=5)        

        self.btnCancelar = tk.Button(self, text='Cancelar')
        self.btnCancelar.config(width=20, font=('ARIAL', 12, 'bold'), fg='white', bg='#FF5733', cursor='hand2', activebackground='#FF0000')
        self.btnCancelar.grid(column=2, row=7, padx=10, pady=5)        

    def guardarPaciente(self):
        Persona = Persona(
            self.svNombre.get()
        )
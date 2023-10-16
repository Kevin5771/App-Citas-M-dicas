import tkinter as tk
from tkinter import messagebox
from paciente.GUI import Frame
import os

#Función Principal
def main():
    root= tk.Tk()
    root.title('App Citas Médicas')
    app = Frame(root)

    app.mainloop()

#Bloque Princiapl
if __name__== '__main__':
    main()
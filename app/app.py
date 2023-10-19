import tkinter as tk
from paciente.GUI import Frame

def main():
    root = tk.Tk()
    root.title('HISTORIA MEDICA')
    root.resizable(0, 0)
    root.iconbitmap('./app/img/clinica.ico')
    frame = Frame(root)
    frame.mainloop()

if __name__ == '__main__':
    main()

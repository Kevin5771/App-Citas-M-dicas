import tkinter as tk
from APP.GUI import Frame


def main():
    root = tk.Tk()
    root.title('App Citas Medicas')
    root.resizable(0, 0)
    root.iconbitmap('./app/img/medicine.ico')
    frame = Frame(root)
    frame.mainloop()

if __name__ == '__main__':
    main()

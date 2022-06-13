import tkinter as tk


def print_hola():
    print('Hola')


def print_adios():
    print('Adios')


win = tk.Tk()
b = tk.Button(win, text='hola', command=print_hola, padx=20, pady=10,
              activebackground='green')
b2 = tk.Button(win, text='adios', command=print_adios, activebackground='red')
b.grid(row=1, column=1)
b2.place(x=300, y=0)
win.geometry("400x400")

win.mainloop()

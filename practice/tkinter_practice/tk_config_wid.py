from tkinter import messagebox
import tkinter as tk

win = tk.Tk()


def hello():
    messagebox.showinfo('from computer', 'hey there')


b = tk.Button(win, text='popup', command=hello)
b.pack()

win.mainloop()

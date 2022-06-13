import tkinter as tk
from functools import partial

win = tk.Tk()


def my_sum(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text=f'sum is: {sum}')


l1 = tk.Label(win, text='First number')
l1.grid(row=1, column=0)
l2 = tk.Label(win, text='Second number')
l2.grid(row=2, column=0)
label = tk.Label(win)
label.grid(row=6, column=2)


x1 = tk.StringVar()
x2 = tk.StringVar()


e1 = tk.Entry(win, textvariable=x1)
e1.grid(row=1, column=2)
e2 = tk.Entry(win, textvariable=x2)
e2.grid(row=2, column=2)

my_sum = partial(my_sum, label, x1, x2)
button = tk.Button(win, text='calculate', command=my_sum)
button.grid(row=3, column=0)

win.mainloop()

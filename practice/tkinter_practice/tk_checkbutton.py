import tkinter as tk


win = tk.Tk()

c1 = tk.IntVar()
c2 = tk.IntVar()

cb1 = tk.Checkbutton(win, text='Music', offvalue=0, onvalue=1, height=5,
                     width=10, variable=c1)
cb2 = tk.Checkbutton(win, text='Sport', offvalue=0, onvalue=1, height=5,
                     width=10, variable=c2)
cb1.pack()
cb2.pack()

var = tk.IntVar()
r1 = tk.Radiobutton(win, text='optional', variable=var, value=1)
r1.pack()

win.mainloop()

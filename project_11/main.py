from tkinter import Button, Tk, Label, StringVar, Listbox, Entry, END


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    a % b


def lcm(a, b):
    lcm = a if a > b else b
    while lcm <= a * b:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm += 1


def hcf(a, b):
    hcf = a if a < b else b
    while hcf >= 1:
        if a % hcf == 0 and b % hcf == 0:
            return hcf
        hcf -= 1


def extract_from_text(text):
    lis = []
    for t in text.split(' '):
        try:
            lis.append(float(t))
        except ValueError:
            pass
    return lis


def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                lis = extract_from_text(text)
                r = operations[word.upper()](lis[0], lis[1])
                my_list.delete(0, END)
                my_list.insert(END, r)
            except Exception:
                my_list.delete(0, END)
                my_list.insert(END, 'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            my_list.delete(0, END)
            my_list.insert(END, 'something went wrong please enter again')


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
              'SUB': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
              'LCM': lcm, 'HCF': hcf, 'PRODUCT': mul, 'MULTIPLICATION': mul,
              'MULTIPLY': mul, 'DIVISION': div, 'DIV': div, 'DIVIDE': div,
              'MOD': mod, 'REMANDER': mod, 'MODULUS': mod}


win = Tk()
win.geometry('500x300')
win.title('Smart Pugger')
win.configure(bg='skyblue')

l1 = Label(win, text='I am a smart calculator', width=20)
l1.place(x=150, y=10)
l2 = Label(win, text='My name is pugger')
l2.place(x=180, y=40)
l3 = Label(win, text='How can i help you')
l3.place(x=176, y=130)

textin = StringVar()
e1 = Entry(win, width=30, textvariable=textin)
e1.place(x=100, y=160)

b1 = Button(win, text='Just This', command=calculate)
b1.place(x=210, y=200)

my_list = Listbox(win, width=20, height=3)
my_list.place(x=150, y=230)

win.mainloop()

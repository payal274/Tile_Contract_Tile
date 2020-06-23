from tkinter import *


root = Tk()
var = IntVar()
var.set(1)

v = IntVar()
v.set(1)


def length(l):
    if var.get() == 1:
        l = l * 3.2808

    elif var.get() ==2:
        l = l * 0.0032808

    return l

def breadth(b):

    if v.get() == 1:
        b = b * 3.2808

    elif v.get() == 2:
        b = b * 0.0032808

    return b


def calculate():

    l = length(float(entry_length.get()))
    b = breadth(float(entry_breadth.get()))
    d = float(entry_discount.get())/100

    tac = l * b
    total_amount = tac * 20
    total_dis=(d * total_amount)
    total_amount = total_amount - total_dis
    tac = str(tac)+"sqft"
    total_amount = str(total_amount) +'$'
    total_dis = str(total_dis)\
                + '$'
    display_all(tac,total_dis,total_amount)


def display_all(tac,total_dis,total_amount):
    label = Label(frame, text="Total Area Covered :")
    label.grid(row=7, column=0)
    listbox = Listbox(frame, width=25, height=1)
    listbox.grid(row=7, column=1)
    listbox.insert(END, tac)
    label = Label(frame, text="Total Discount :")
    label.grid(row=8, column=0)
    listbox = Listbox(frame, width=25, height=1)
    listbox.grid(row=8, column=1)
    listbox.insert(END, total_dis)
    label = Label(frame, text="Total Amount:")
    label.grid(row=9, column=0)
    listbox = Listbox(frame, width=25, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, total_amount)



canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()

        frame.place(relx=0.45, rely=0.1, relwidth=0.8, relheight=0.8)
        label = Label(frame, text="Tile Contractor App")
        label.grid(row=0, column=1)

label = Label(frame, text="Length :")
label.grid(row=1, column=0)

entry_length = Entry(frame)
entry_length.grid(row=1, column=1)

ra = Radiobutton(frame, text="Metre", variable=var, value=1)
ra.grid(row=2, column=1, sticky=W)
ra1 = Radiobutton(frame, text="Milimeter", variable=var, value=2)
ra1.grid(row=2, column=2, sticky=W)
ra2 = Radiobutton(frame, text="Feet", variable=var, value=3)
ra2.grid(row=2, column=3, sticky=W)


label = Label(frame, text="Breadth :")
label.grid(row=3, column=0)

entry_breadth = Entry(frame)
entry_breadth.grid(row=3, column=1)

ra = Radiobutton(frame, text="Metre", variable=v, value=1)
ra.grid(row=4, column=1, sticky=W)
ra1 = Radiobutton(frame, text="Milimeter", variable=v, value=2)
ra1.grid(row=4, column=2, sticky=W)
ra2 = Radiobutton(frame, text="Feet", variable=v, value=3)
ra2.grid(row=4, column=3, sticky=W)

label = Label(frame, text="Discount :")
label.grid(row=5, column=0)

entry_discount = Entry(frame)
entry_discount.grid(row=5, column=1)

button = Button(frame, text="Pay", command=calculate)
button.grid(row=6, column=1)


root.mainloop()

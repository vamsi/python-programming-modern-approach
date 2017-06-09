from tkinter import *


def callback():
    label.configure(text='Button clicked')


root = Tk()
label = Label(text='Not clicked')
button = Button(text='Click me', command=callback)
label.grid(row=0, column=0)
button.grid(row=1, column=0)
root.mainloop()

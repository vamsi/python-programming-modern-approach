from tkinter import *


def callback(r, c):
    global player
    if player == 'X':
        b[r][c].configure(text='X')
        player = 'O'
    else:
        b[r][c].configure(text='O')
        player = 'X'


root = Tk()
b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]
     ]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3,
                         bg='yellow', command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

player = 'X'
root.mainloop()

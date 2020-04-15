#_[N_F]_

from tkinter import Label, Button, Entry, Tk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '!', '@',
            '#', '$', '%', '*', '(', ')', '_', '+', '-', '=', '§', ':', '?',
            ';', '/', 'ª', 'º', '°', '>', '<', '.', ',', '|']

root = Tk()


def click():
    password = str(box.get())
    length = len(password)
    poss = len(alphabet) ** length
    time = poss / (2500 * length)
    label['text'] = "{}s".format(int(time))

box = Entry(root, font='arial 12', width=30)
box.place(x=10, y=15)

button = Button(root, font='arial 12', width=30, text="GO!", command=click)
button.place(x=10, y=75)

label = Label(root, font='arial 12', width=30, text="time", relief='solid')
label.place(x=10, y=155)


root.geometry("300x300")
root.mainloop()

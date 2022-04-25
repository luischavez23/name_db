from tkinter import ttk
from tkinter import *


class Person: 
    def __init__(self, window):
        self.window = window
        self.window.title('Register GUI')

        frame = LabelFrame(self.window, text='Register')
        frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

        Label(frame, text='Name: ').grid(row=1, column=0, padx=10, pady=5)
        self.mcode = Entry(frame)
        self.mcode.grid(row=1, column=1, padx=10)
        self.mcode.focus()
        
        Label(frame, text='Last name:').grid(row=2, column=0)
        self.age = Entry(frame)
        self.age.grid(row=2, column=1)

        ttk.Button(frame, text='Submit').grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipady=5, sticky= W + E)


if __name__ == '__main__':
    root = Tk()
    app = Person(root)
    root.mainloop()
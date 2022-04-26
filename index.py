from tkinter import ttk
from tkinter import *

import sqlite3


class Person:

    def __init__(self, window):
        self.db_name = 'database.db' 

        self.window = window
        self.window.title('Register GUI')
        self.window.geometry('480x415')

        frame = LabelFrame(self.window, text='Register')
        frame.grid(row=0, column=0, columnspan=3, pady=(20,0), padx=20)

        Label(frame, text='Name: ').grid(row=1, column=0, padx=10, pady=5)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1, padx=10)
        self.name.focus()
        
        Label(frame, text='Last name:').grid(row=2, column=0)
        self.last_name = Entry(frame)
        self.last_name.grid(row=2, column=1)

        ttk.Button(frame, text='Submit', command=self.add_names).grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipady=5, sticky= W + E)
        
        self.message = Label(text='')
        self.message.grid(row=4, column=0, columnspan=2, pady=5)
        
        self.table = ttk.Treeview(height=10, columns=("#0","#1"))
        self.table.grid(row=5, column=0, padx=8)
        self.table.heading('#0', text='#', anchor=CENTER)
        self.table.heading('#1', text='Name', anchor=CENTER)
        self.table.heading('#2',text='Last name', anchor=CENTER)
        self.table.column('#0',width=60)

    
    def run_sentence( self, sentence, parameters = () ):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(sentence, parameters)
            conn.commit()
        return result
        
    def validation( self ):
        return self.name.get() == '' or self.last_name.get() == ''
        
    def create_table( self ):
        sentence = """CREATE TABLE IF NOT EXISTS person (
                        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        LAST_NAME TEXT)
                    """
        self.run_sentence(sentence)

    def clear_fields(self):
        self.name.delete(0, END)
        self.last_name.delete(0, END)
        self.name.focus()

    def add_names( self ):
        name = self.name.get().strip()
        last_name = self.last_name.get().strip()
        
        if not self.validation():
            self.create_table()
            sentence = 'INSERT INTO person VALUES (NULL, ?, ?)'
            parameters = (name, last_name)
            self.run_sentence(sentence, parameters)
            self.message['text'] = f'{name} {last_name} - Registered Succesfully'
            self.message.config(fg= '#000fff000')
            self.clear_fields()
            return
        else:
            self.message['text'] = 'Please fill both field'
            self.message.config(fg= '#fff000000')
        
            

if __name__ == '__main__':
    root = Tk()
    app = Person(root)
    root.mainloop()
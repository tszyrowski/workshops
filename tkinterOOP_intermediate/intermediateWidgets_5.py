'''
Created on 13 Jul 2017

@author: T

themes:
ttk.Style().theme_names()
ttk.Style().theme_use(style)

>>> import tkinter.ttk
>>> print(tkinter.ttk.Style().theme_names())
('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
'''
from tkinter import *
from tkinter.ttk import *

class TkNotebook():
    def __init__(self, root):
        
        self.frame = Frame(root)
        self.notebook = Notebook(self.frame)
        
        f1 = Frame(self.notebook, width=200, height=100)        
        f2 = Frame(self.notebook, width=200, height=100)
        f3 = Frame(self.notebook, width=200, height=100)
        self.notebook.add(f1, text="Page 1")
        self.notebook.add(f2, text="Page 2")
        self.notebook.add(f3, text="Tree")
        
        self.label = Label(self.frame, text="A Notebook on the left")
        
        self.lbl1 = Label(f1, text="ble")
        self.lbl1.pack()
        
        self.column_treeview(f2)
        self.tree_treeview(f3)
        
        self.frame.grid(row=0, column=0, sticky=(N,S,E,W))
        self.notebook.grid(row=0, column=0, sticky=(N,S,E,W))
        self.label.grid(row=0, column=1, sticky=(E,))
        
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame.rowconfigure(0,weight=2) #  row 0 is the one which will grow
        self.frame.columnconfigure(0, weight=2)
        
    def column_treeview(self, parent):    
        columns = ("Name", "Description")
        self.ctree = Treeview(parent, columns=columns, show="headings")
        # adjust width and names for the column
        for col in columns:
            self.ctree.column(col, width=90)
            self.ctree.heading(col, text=col)
        # insert data    
        self.ctree.insert("","end", values=["Example", "One orw"])
        self.ctree.insert("","end", values=["Example", "sec orw"])
        
        # pack will fill all page
        self.ctree.pack(fill=BOTH, expand=1)
        
    def tree_treeview(self, parent):
        self.ttree = Treeview(parent)
        
        id = self.ttree.insert("", "end", text="Example")
        self.ttree.insert(id, "end", text="first sub item")
        
        id = self.ttree.insert("", "end", text="Example")
        self.ttree.insert(id, "end", text="first sub item")
        
        self.ttree.pack(fill=BOTH, expand=1)

if __name__ == '__main__':
    root = Tk()
    myApp = TkNotebook(root)
    root.mainloop()
    
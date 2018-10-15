'''
@author: T
'''
#from Tkinter import *   # works for Python 2.7
from tkinter import *   # works for Python 3.x

root = Tk()             # main application

# create a widget w
w = Label(root, text="Hello, world")
w.pack()                # place the widget w inside application

root.mainloop()         # start application loop
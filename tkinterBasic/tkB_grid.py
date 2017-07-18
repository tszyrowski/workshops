'''
Created on 16 Jul 2017

@author: T
'''
import tkinter as tk

myColours = ['red','green','orange','white','yellow','blue']

r = 0
for c in myColours:
    tk.Label(text=c, relief='ridge',width=15).grid(row=r, column=0)
    tk.Entry(bg=c, relief='sunken',width=10).grid(row=r, column=1)
    r = r+1

tk.mainloop()
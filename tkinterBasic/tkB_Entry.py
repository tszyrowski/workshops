'''
Created on 15 Jul 2017

@author: T
'''

import tkinter as tk

root = tk.Tk()              # make a base for the app

def myEntries():            # function to be called after tick
    print(entry1.get(), entry2.get())

lbl1 = tk.Label(root, text='name')
lbl1.grid(row=0, sticky='E')

lbl2 = tk.Label(root,text='Password')
lbl2.grid(row=1)

entry1 = tk.Entry(root)     # field for input
entry1.grid(row=0, column=1)
entry1.focus_set()          # be the first field to fill

entry2 = tk.Entry(root, show='*', bg='white')
entry2.grid(row=1, column=1)
 
chk = tk.Checkbutton(root, text="Keep me logged", command=myEntries)
chk.grid(columnspan=2)

if __name__ == '__main__':
    root.mainloop()         # start application
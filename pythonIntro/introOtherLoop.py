'''
@author: T
'''
import tkinter as tk    # getting GUI library (module)
root = tk.Tk()          # create main application structure (class)
g = tk.Canvas()         # create place to draw things in   
g.pack()                # place canvas inside application 

r = 10                  # create radius of a ball
y = 30                  # y-coordinate
colors = ['red', 'green', 'blue'] # list of colours to use 

for i in range(1,11):       # main (outside) loop
    print(i)
    x = 30
    for j in range(1,i):    # second (inner) loop
        if i < 4:           # execute for first loops
            g.create_oval(x-r, y-r, x+r, y+r, fill=colors[0])
        elif 4 < i < 9:     # execute middle loops
            g.create_oval(x-r, y-r, x+r, y+r, fill=colors[1])
        else:               # all else
            g.create_oval(x-r, y-r, x+r, y+r, fill=colors[2])
        x += 2 * r          # move x-coordinate
    y += 2 * r              # move y-coordinate
root.mainloop()             # execution application
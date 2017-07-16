'''
Created on 16 Jul 2017

@author: T
'''
import tkinter as tk
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()

blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill="red")
grenbox = canvas.create_rectangle(25,25,130,60, fill="green")

# canvas.delete(redline)
# canvas.delete('all')

photo = tk.PhotoImage(file='C:\\Users\\T\\Pictures\\yacht.png')
lbl = tk.Label(root, image=photo)
lbl.pack()

if __name__ == '__main__':
    root.mainloop()
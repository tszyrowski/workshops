'''
Created on 15 Jul 2017

@author: T
'''
import tkinter as tk

root = tk.Tk()              # make a base for the app
# create labels
lblOne = tk.Label(root, text="This is my first label")
lblTwo = tk.Label(root, text="Second one", bg='green', fg='black')
lblThree = tk.Label(root, text="Three", bg='blue', fg='black')
# place labels inside application
lblOne.pack(padx=10, pady=10)
lblTwo.pack(fill="x")
lblThree.pack(side='left', fill="y")

if __name__ == '__main__':
    root.mainloop()         # start application
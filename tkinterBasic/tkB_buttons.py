'''
Created on 15 Jul 2017

@author: T
'''
import tkinter as tk
root = tk.Tk()

def printName(): print('Hello')   
def print2Name(event): print(event, 'from event')   
def print3Name(event): print(event, 'btn 3')   
def leftClick(event): print('left')   
def rightClick(event): print('right')    
def middleClick(event): print('Middle')
        
btn1 = tk.Button(root, text="Print name", command=printName).pack()
 
btn2 = tk.Button(root, text='Second btn')
btn2.bind("<Button-1>", print2Name) # bind to left click
btn2.pack()
 
btn3 = tk.Button(root, text='Third button')
btn3.bind("<Button-3>", print3Name) # bind to right click
btn3.pack()
 
frame = tk.Frame(root, width=300, height=250, bd=1, relief="sunken")
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", rightClick)
frame.bind("<Button-3>", middleClick)
frame.pack()

if __name__ == '__main__':
    root.mainloop()
'''
Created on 15 Jul 2017

@author: T
'''
import tkinter as tk
import math
from numpy import square

def evaluate(event):                    # function to evaluate square root
    number = float(inputNumber.get())   # read what variable entry stores
    print(number, type(number))         # and convert it to float 
    squareRoot = math.sqrt(number)      # calculate square root
    result.configure(text="Square root of: "+str(number)+'\n is: '+str(squareRoot))
    
root = tk.Tk()
lbl = tk.Label(root, text="Number to take square root:").pack()
inputNumber = tk.Entry(root)
inputNumber.bind("<Return>", evaluate)
inputNumber.pack()

result = tk.Label(lbl)
result.pack()

root.mainloop()
import tkinter as tk
import math

root = tk.Tk()

def calculateSqRootFromUserInput(event):
    result = str(math.sqrt(float(input.get())))
    output.delete(0, tk.END)
    output.insert(0, result)

tk.Label(root, text='Number to take square root:').pack()

input = tk.Entry(root)
input.pack()
input.focus_set()


tk.Label(root, text='Square root is:').pack()

output = tk.Entry(root)
output.pack()

input.bind("<Return>", calculateSqRootFromUserInput)

root.mainloop()

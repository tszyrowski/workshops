import tkinter as tk

root = tk.Tk()

def calculateSqRootFromUserInput(event):
    print(input.get())

tk.Label(root, text='Number to take square root:').pack()

input = tk.Entry(root)
input.pack()
input.focus_set()

input.bind("<Return>", calculateSqRootFromUserInput)

root.mainloop()

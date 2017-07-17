import tkinter as tk

root = tk.Tk()

tk.Label(root, text='Number to take square root:').pack()

input = tk.Entry(root)
input.pack()
input.focus_set()

root.mainloop()

import tkinter as tk
root = tk.Tk()

def menuClickHandler():
    print('clicked in menu')

menu = tk.Menu(root)
root.config(menu=menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open Project", command=menuClickHandler)
fileMenu.add_command(label="New Project", command=menuClickHandler)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Make a bomb", command=menuClickHandler)

toolBar = tk.Frame(root, bg="orange")
insertButt = tk.Button(toolBar, text="imande", command=menuClickHandler)
insertButt.pack(side="left", padx = 2, pady = 2)
insertButt = tk.Button(toolBar, text="print", command=menuClickHandler)
insertButt.pack(side="left", padx = 2, pady = 2)
toolBar.pack(side="top", fill="x")



root.mainloop()

import tkinter as tk

root = tk.Tk()              # make a base for the app

mn = tk.Menu(root)      # menu bar
root.config(menu=mn)


def doNothing():
    pass

subMn = tk.Menu(mn)     # submenu
mn.add_cascade(label="File", menu=subMn)
subMn.add_command(label="new project", command=doNothing)
subMn.add_command(label="New", command=doNothing)
subMn.add_separator()
subMn.add_command(label="Exit", command=root.quit)

editMn = tk.Menu(mn)
mn.add_cascade(label="Edit", menu=editMn)

toolBar = tk.Frame(root, bg='blue')
insertButt = tk.Button(toolBar, text="validate", command=doNothing)
insertButt.pack(side="left", padx=2, pady=2)
printButt = tk.Button(toolBar, text="print", command=doNothing)
printButt.pack(side="left", padx=2, pady=2)
toolBar.pack(side="top", fill="x")
# statusbar
status = tk.Label(root, text="Prepare to do nothing..", bd=1, relief="sunken", anchor="w")
status.pack(side="bottom", fill="x")


if __name__ == '__main__':
    root.mainloop()         # start application

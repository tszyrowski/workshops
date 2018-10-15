import tkinter as tk

root = tk.Tk()              # make a base for the app
# create labels
lblOne = tk.Label(root, text="This is my first label")
lblTwo = tk.Label(root, text="Second", bg='green', fg='black')
lblThree = tk.Label(root, text="Three", bg='blue', fg='black')
# place labels inside application
lblOne.pack()
lblTwo.pack(fill="x")   # 'x' means expand horizontally,
                        # 'y' vertically, 'BOTH' all space
lblThree.pack(side='left', fill="y")

if __name__ == '__main__':
    root.mainloop()         # start application
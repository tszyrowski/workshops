import tkinter.messagebox

tkinter.messagebox.showinfo("WindTilte", message="wind title message")

answer = tkinter.messagebox.askquestion("Yes or no?", "Yes or no bro?")
if answer == "yes":
    print("clicked yes")

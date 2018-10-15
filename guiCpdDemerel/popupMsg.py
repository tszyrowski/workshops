'''
Created on 15 Oct 2018

@author: T
'''
import tkinter.messagebox
# does not work without explicit import
import tkinter as tk

root = tk.Tk()              # make a base for the app

def yesFunc():
    print("clicked yes")
# basic messagebox
tkinter.messagebox.showinfo("WindTilte", message="this is some message")

# question to answer yes/no
answer = tkinter.messagebox.askquestion("Question 1", "what do anser")
if answer == "yes":
    yesFunc()

# another type of message    
ans2 = tkinter.messagebox.askyesnocancel('title', 'Triple question')
print(ans2)


if __name__ == '__main__':
    root.mainloop()         # start application
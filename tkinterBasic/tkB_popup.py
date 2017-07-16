'''
Created on 16 Jul 2017

@author: T
'''
import tkinter.messagebox
# does not work without explicit import

# basic messagebox
tkinter.messagebox.showinfo("WindTilte", message="this is some message")

# question to answer yes/no
answer = tkinter.messagebox.askquestion("Question 1", "what do anser")
if answer == "yes":
    print("clicked yes")

# another type of message    
ans2 = tkinter.messagebox.askyesnocancel('title', 'Triple question')
print(ans2)
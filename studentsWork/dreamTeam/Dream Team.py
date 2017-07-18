# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:58:44 2017

@author: visitor007
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:39:36 2017

@author: visitor007
"""

import tkinter as tk
import time



def question1(event):
    
    answer = float(userInput1.get())
    if answer == 22:
        result = "Correct"
        colour = "green"
        
    else:
        result = "Incorrect"  
        colour = "red"
        
    outputLabel1.configure(text = result, background = colour, fg = "yellow")
    calcScore()
    
def question2(event):
    
    answer = userInput2.get()
    if answer == "Paris" or answer == "paris":
        result = "Correct"
        colour = "green"
        
        
        
    else:
        result = "Incorrect"  
        colour = "red"
        
    outputLabel2.configure(text = result, background = colour,fg = "yellow")
    calcScore()
    
def question3(event):
    
    answer = userInput3.get()
    if answer == "Keywords" or answer == "keywords":
        result = "Correct"
        colour = "green"        
    else:
        result = "Incorrect"  
        colour = "red"
        
    outputLabel3.configure(text = result, background = colour , fg = "Yellow")
    calcScore()

def calcScore():
    score = 0 
    answer = float(userInput1.get())
    if answer == 22:
        score+=1
        print(score)
    
    answer = userInput2.get() 
    if answer == "Paris" or answer == "paris":
        score += 1
    
    answer = userInput3.get()
    if answer == "Keywords" or answer == "keywords":
        score += 1
    
    if score == 3:
        colour = "green"
    elif score == 2:
        colour = "orange"
    else:
        colour = "red"
        
    Score.configure(text = "Your current Total is: " + str(score), background = colour)

root = tk.Tk()
root.title("Quiz")
root.minsize(width=300, height=300)
root.configure(background = "yellow")

label1 = tk.Label(root, text = "What is 10 kilos in pounds? (1KG = 2.2lbs)", background = "yellow", font = "arial").pack()

userInput1 =  tk.Entry(root)
userInput1.bind("<Return>", question1, calcScore)
userInput1.pack()

outputLabel1 = tk.Label(label1, background = "grey")
outputLabel1.pack()

label2 = tk.Label(root, text = "What is the capital city of France?", background = "yellow", font = "arial").pack()

userInput2 =  tk.Entry(root)
userInput2.bind("<Return>", question2, calcScore)
userInput2.pack()

outputLabel2 = tk.Label(label1, background = "yellow")
outputLabel2.pack()

label3 = tk.Label(root, text = "What does Python have 33 of?", background = "yellow", font = "arial").pack()

userInput3 =  tk.Entry(root)
userInput3.bind("<Return>", question3, calcScore)
userInput3.pack()

outputLabel3 = tk.Label(label1, background = "yellow")
outputLabel3.pack()

Score = tk.Label(label1, pady = 2)
Score.pack()





if __name__ == '__main__':
    root.mainloop()
import tkinter as tk
import random

root = tk.Tk()
student = 0

students = ["Sally", "Joe", "Fred", "Jenny", "Bob", "Polly", "Amy"]

def choose_student(event):    
    
    choice = random.randint(0,(len(students)-1))
    student = (students[choice])
    print(student)
    return student
    
student = choose_student(students)
#print(chosen_student)

lbl1 = tk.Label(root, text="Add your question")
lbl1.grid(row=0)

entry1 = tk.Text(root, width=70, height=3)
entry1.grid(row = 0, column = 1)
entry1.focus_set()

btn1 = tk.Button(root, text="Random name", command = choose_student)
btn1.grid(row=2)

lbl2 = tk.Label(root, text=student)
lbl2.grid(column=1)




root.mainloop()


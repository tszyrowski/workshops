'''
Application to display GUI, allow login, validate and add new entry
'''
import tkinter as tk
import tkinter.filedialog as filedlg # implicit import to avoid IDE conf
from tkinter import ttk
import csv

root = tk.Tk()                             # create main app
root.title("CPD - Damerel")

def callPopUp():
    ''' opens a pop-up window to choose the file with students'''
    filename = filedlg.askopenfilename(initialdir = "../stingsAndFiles/studentsData.csv")
    data = []
    with open(filename, 'r') as dataFile:
        reader = csv.reader(dataFile)
        for row in reader:
            data.append(row)
    for row in data:
        name = row[0]
        surname = row[1]
        email = row[2]
        passwword = row[3]
        tree.insert("",0,values=(name,surname,email,passwword))
    return data

def saveChanges():
    ''' save changes to file '''
    print('changes saved')

# Add menu to get pop-up to a file
mn = tk.Menu(root)
root.config(menu=mn)

subMn = tk.Menu(mn)                         # add entry to menu
mn.add_cascade(label="File", menu=subMn)
subMn.add_command(label='open', command=callPopUp)
subMn.add_command(label='save', command=saveChanges)

# Add canvas to display file with entries
TableMargin = tk.Frame(root, width=500)
TableMargin.pack(side='top')
scrollbary = ttk.Scrollbar(TableMargin, orient='vertical')
tree = ttk.Treeview(root, columns=['name','surname','email','password'], yscrollcommand=scrollbary.set)
tree.heading('name', text='Name', anchor='w')
tree.heading('surname', text='Surname', anchor='w')
tree.heading('email', text='Email', anchor='w')
tree.heading('password', text='Passowrd', anchor='w')
tree.column('#0', stretch='no', minwidth=0, width=0)
tree.column('#1', stretch='no', minwidth=0, width=200)
tree.column('#2', stretch='no', minwidth=0, width=200)
tree.column('#3', stretch='no', minwidth=0, width=300)
tree.column('#4', stretch='no', minwidth=0, width=300)
tree.pack()

if __name__=="__main__":
    root.mainloop()
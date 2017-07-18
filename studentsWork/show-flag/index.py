import tkinter as tk
import pycountry

root = tk.Tk()

def showFlag(event):
    countryName = input.get()
    country = pycountry.countries.get(name=countryName)
    flagImgPath = "./flagopedia/%s.png" %(country.alpha_2.lower())
    print(flagImgPath)
    photo2 = tk.PhotoImage(file=flagImgPath)
    lbl.configure(image=photo2)
    lbl.myass = photo2

tk.Label(root, text = "enter county name to see it's flag").pack()

input = tk.Entry(root)
input.pack()
input.focus_set()
input.bind("<Return>", showFlag)

photo = tk.PhotoImage(file='./All-Flags.png')
lbl = tk.Label(root, image=photo)
lbl.pack()

root.mainloop()

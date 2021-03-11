from tkinter import *

root= Tk()



def click():
    CatIndex = input("please select the id: ")



mybutton=Button(root, text="click me", command=click)
mybutton.pack()






root.mainloop()
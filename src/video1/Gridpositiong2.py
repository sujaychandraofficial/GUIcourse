from tkinter import *

root=Tk()
mylabel1=Label(root,text="hello world")
mylabel2=Label(root,text="my name is sujay")
mylabel3=Label(root,text="simple gui leaerning")
mylabel4=Label(root,text="pattern gui")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)
mylabel3.grid(row=2,column=0)
mylabel4.grid(row=4,column=1)


root.mainloop()

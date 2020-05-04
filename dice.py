
from tkinter import*
import random
root=Tk()
def roll():
    value= random.randint(1,6)
    global photo
    if value==1:
        
        photo=PhotoImage(file=r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32\PIL\dice1.png")
    if value==2:
        photo=PhotoImage(file=r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32\PIL\dice2.png")
    if value==3:
        
        photo=PhotoImage(file=r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32\PIL\dice3.png")

    if value==4:
        photo=PhotoImage(file=r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32\PIL\dice4.png")

    if value==5:
        photo=PhotoImage(file=r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32\PIL\dice5.png")
    if value==6:
        photo=PhotoImage(file=r"C:\Users\HP\AppData\Local\Programs\Python\Python38-32\PIL\dice6.png")

    Label(root, image=photo).grid(row=3,column=0) 
rollbtn=Button(text="roll",command=roll,bd=10,width=25,bg="light blue")
rollbtn.grid(row=0,column=0)
root.mainloop()



from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.state('zoomed')
img=PhotoImage(file="Bus_for_Project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=30)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=30,padx=440)
Label(root,text="Check Your Booking",font=("Ariel",20),bg="light green",fg="green" ).grid(row=2,column=0,columnspan=30,padx=400,pady=50)
Label(root,text="Enter Your Mobile No:",font=("Ariel")).grid(row=3,column=5,columnspan=14)
Enter=Entry(root,font=("Ariel",16),width=12).grid(row=3,column=6,columnspan=19)

Button(root,text="Check Booking",font=('Ariel',16)).grid(row=3,column=15,columnspan=8)

root.mainloop()





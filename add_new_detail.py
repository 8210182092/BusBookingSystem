from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.state('zoomed')
root.geometry()
img=PhotoImage(file=".\\Bus_For_Project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=20)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=10,padx=440)
Label(root,text="Add New Details to DataBase",font=("Ariel",20),fg="green4" ).grid(row=2,column=0,columnspan=20,padx=400,pady=50)
def close():
    root.destroy()
    import Add_Bus_Operator_Detail
b1=Button(root,text="New Operator",font=('Ariel',16),bg="light green",command=close).grid(row=3,column=1,padx=20)
def close1():
    root.destroy()
    import Add_Bus_Detail
b2=Button(root,text="New Bus",font=('Ariel',16),bg="orange red",command=close1).grid(row=3,column=2,padx=20)
def close2():
    root.destroy()
    import Add_Bus_Route_Detail
b3=Button(root,text="New Route",font=('Ariel',16),bg="steel blue",command=close2).grid(row=3,column=3,padx=8)
def close3():
    root.destroy()
    import Add_Bus_Running_Detail
b4=Button(root,text="New Run",font=('Ariel',16),bg="RosyBrown4",command=close3).grid(row=3,column=4,padx=10)


root.mainloop()

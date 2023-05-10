from tkinter import *
root=Tk()
root.state('zoomed')
img=PhotoImage(file=".\\Bus_for_Project.png")
img1=PhotoImage(file=".\\home (1).png")
Label(root,image=img).grid(row=0,column=0,columnspan=40)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=30,padx=440)
Label(root,text="Add Bus Operator Details",font=("Ariel",20),bg="green",fg="light green" ).grid(row=2,column=0,columnspan=30,padx=400,pady=50)
Operator=Label(root,text="Operator Id",font=("Ariel")).grid(row=3,column=2,columnspan=2)
Operator=Entry(root,font=("Ariel",13),width=6).grid(row=3,column=2,columnspan=6)
Name=Label(root,text="Name",font=("Ariel")).grid(row=3,column=3,columnspan=7)
Name=Entry(root,font=("Ariel",13)).grid(row=3,column=4,columnspan=10)
Address=Label(root,text="Address",font=("Ariel")).grid(row=3,column=6,columnspan=12)
Address=Entry(root,font=("Ariel",13),width=13).grid(row=3,column=6,columnspan=16)
Phone=Label(root,text="Phone",font=("Ariel")).grid(row=3,column=7,columnspan=18)
Phone=Entry(root,font=("Ariel",13),width=11).grid(row=3,column=8,columnspan=20)
Email=Label(root,text="Email",font=("Ariel")).grid(row=3,column=10,columnspan=21)
Email=Entry(root,font=("Ariel",13)).grid(row=3,column=15,columnspan=30)
b1=Button(root,text="Add",font=('Ariel',16),bg="light green").grid(row=3,column=19,columnspan=31)
b2=Button(root,text="Edit",font=('Ariel',16),bg="light green").grid(row=3,column=22,columnspan=32)
def close():
    root.destroy()
    import home
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=4,column=10,columnspan=32)
root.mainloop()












from tkinter import *
root=Tk()
root.state('zoomed')
img=PhotoImage(file=".\\Bus_for_Project.png")
img1=PhotoImage(file=".\\home (1).png")
Label(root,image=img).grid(row=0,column=0,columnspan=40)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=30,padx=440)
Label(root,text="Add Bus Details",font=("Ariel",20),bg="green",fg="light green" ).grid(row=2,column=0,columnspan=30,padx=400,pady=50)
Route=Label(root,text="Route id",font=("Ariel")).grid(row=3,column=4)
Routr=Entry(root,font=("Ariel")).grid(row=3,column=5)
Station=Label(root,text="Station Name",font=("Ariel")).grid(row=3,column=6)
Station=Entry(root,font=("Ariel")).grid(row=3,column=7)
Station=Label(root,text="Station Id",font=("Ariel")).grid(row=3,column=8)
Station=Entry(root,font=("Ariel")).grid(row=3,column=9)
b1=Button(root,text="Add Route",font=('Ariel',16),bg="light green").grid(row=3,column=10)
b2=Button(root,text="Delete Route",font=('Ariel',16),bg="light green",fg="red").grid(row=3,column=11)
def close():
    root.destroy()
    import home
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=4,column=8,columnspan=28,pady=30)


root.mainloop()


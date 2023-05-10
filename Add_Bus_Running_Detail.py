from tkinter import *
root=Tk()
root.state('zoomed')
img=PhotoImage(file=".\\Bus_for_project.png")
img1=PhotoImage(file=".\\home (1).png")
Label(root,image=img).grid(row=0,column=0,columnspan=40)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=30,padx=440)
Label(root,text="Add Bus Running Details",font=("Ariel",20),bg="green",fg="light green" ).grid(row=2,column=0,columnspan=30,padx=400,pady=50)
Bus=Label(root,text="Bus ID",font=("Ariel")).grid(row=3,column=4,pady=40)
Bus=Entry(root,font=("Ariel")).grid(row=3,column=5)
Running=Label(root,text="Running Date",font=("Ariel")).grid(row=3,column=6)
Running=Entry(root,font=("Ariel")).grid(row=3,column=7)
Seat=Label(root,text="Seat Available",font=("Ariel")).grid(row=3,column=8)
Seat=Entry(root,font=("Ariel")).grid(row=3,column=9)
b1=Button(root,text="Add Run",font=('Ariel',16),bg="light green").grid(row=3,column=10)
b2=Button(root,text="Delete Run",font=('Ariel',16),bg="light green",fg="red").grid(row=3,column=11)
def close():
    root.destroy()
    import home
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=4,column=9,columnspan=28,pady=30)

root.mainloop()




from tkinter import*
from tkinter.messagebox import* 
root=Tk()
root.state('zoomed')
img=PhotoImage(file=".\\Bus_for_project.png")
img1=PhotoImage(file="home (1).png")
Label(root,image=img).grid(row=0,column=0,columnspan=24)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=30,padx=440)
Label(root,text="Add Bus Details",font=("Ariel",20),bg="green",fg="light green" ).grid(row=2,column=0,columnspan=30,padx=400,pady=50)
BusID=Label(root,text="Bus ID",font=("Ariel")).grid(row=3,column=3,pady=40)
BusID=Entry(root,font=("Ariel"),width=10).grid(row=3,column=4)
bustype=Label(root,text='bustype',font='Ariel').grid(row=3,column=5)
bustype=StringVar()
opt=['2x2','Ac 2x2']
d_menu=OptionMenu(root,bustype,*opt).grid(row=3,column=6)
Capacity=Label(root,text="Capacity",font=("Ariel")).grid(row=3,column=7)
Capacity=Entry(root,font=("Ariel"),width=10).grid(row=3,column=8)
FareRs=Label(root,text="Fare Rs",font=("Ariel")).grid(row=3,column=9)
FareRs=Entry(root,font=("Ariel"),width=10).grid(row=3,column=10)
Operator=Label(root,text="Operator ID",font=("Ariel")).grid(row=3,column=11)
Operator=Entry(root,font=("Ariel"),width=10).grid(row=3,column=12)
Route=Label(root,text="Route id",font=("Ariel")).grid(row=3,column=13)
Routr=Entry(root,font=("Ariel"),width=10).grid(row=3,column=14)
b1=Button(root,text="Add Bus",font=('Ariel',16),bg="light green").grid(row=4,column=9,pady=40)
b2=Button(root,text="Edit Bus",font=('Ariel',16),bg="light green").grid(row=4,column=10)
def close():
    root.destroy()
    import home
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=4,column=7,columnspan=28)

root.mainloop()


